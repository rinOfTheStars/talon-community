from talon import Context, Module, actions

ctx = Context()
mod = Module()

mod.tag(
    "code_annotations_and_macros",
    desc="Enables annotation/macro language functionality",
)

# Java Annotations are grouped in w/ macros, even though they are fairly different functionality-wise
mod.list(
    "code_basic_macros",
    desc="A list of single-line annotations/macros without any parameters (ex: Swift's `@Observable`; Java's `@FunctionalInterface`)",
)
mod.list(
    "code_function_macros",
    desc="A list of annotations/macros which take parameters as if they were functions (ex: Rust's `print!`)",
)
mod.list(
    "code_array_macros",
    desc="A list of annotations/macros which take parameters as if they were arrays/lists (ex: Rust's `vec!`)",
)
mod.list(
    "code_block_macros",
    desc="A list of annotations/macros which take a code block as their (usually sole) parameter(s) (ex: Rust's `macro_rules!`)",
)

ctx.matches = r"""
tag: user.code_annotations_and_macros
"""

basic_macros = {}
function_macros = {}
array_macros = {}
block_macros = {}

ctx.lists["user.code_basic_macros"] = basic_macros
ctx.lists["user.code_function_macros"] = function_macros
ctx.lists["user.code_array_macros"] = array_macros
ctx.lists["user.code_block_macros"] = block_macros


# Direct clone of code_insert_function_or_macro implementation in rust.py
def do_macro_insert(text: str, selection: str, left_delim: str, right_delim: str):
    if selection:
        out_text = text + f"{left_delim}{selection}{right_delim}"
    else:
        out_text = text + f"{left_delim}{right_delim}"
    actions.user.paste(out_text)
    actions.edit.left()


@mod.capture(rule="{user.code_basic_macros}")
def code_basic_macros(m) -> str:
    "A basic annotation/macro"
    return m.code_basic_macros


@mod.capture(rule="{code_function_macros}")
def code_function_macros(m) -> str:
    "A function-like annotation/macro"
    return m.code_function_macros


@mod.capture(rule="{code_array_macros}")
def code_array_macros(m) -> str:
    "A array-like annotation/macro"
    return m.code_array_macros


@mod.capture(rule="{code_block_macros}")
def code_block_macros(m) -> str:
    "A block annotation/macro"
    return m.code_block_macros


@mod.action_class
class Actions:
    def code_insert_basic_macro(text: str):
        """Insert a basic annotation/macro at the cursor."""
        actions.user.paste(text)
        actions.edit.left()

    def code_insert_function_macro(text: str, selection: str):
        """
        Insert a function-like annotation/macro and position the cursor appropriately.
        Overload this if the language does not use `()` as the function parameter delimiter pair.
        """
        do_macro_insert(text, selection, "(", ")")

    def code_insert_macro_array(text: str, selection: str):
        """
        Insert a array-like annotation/macro and position the cursor appropriately.
        Overload this if the language does not use `[]` as the array delimiter pair.
        """
        do_macro_insert(text, selection, "[", "]")

    def code_insert_macro_block(text: str, selection: str):
        """
        Insert a code block based annotation/macro and position the cursor appropriately.
        Overload this if the language does not use `{}` as the array delimiter pair.
        """
        do_macro_insert(text, selection, "{", "}")
