from talon import Context, Module

mod = Module()

ctx = Context()
ctx.matches = r"""
code.language: swift
"""

# Action class #


@mod.action_class
class Actions:
    def call_common_snippets():
        """todo"""


# Lists and Captures #


# Types

number_types = {
    "int": "Int",
    "int eight": "Int8",
    "int sixteen": "Int16",
    "int thirty two": "Int32",
    "int sixty four": "Int64",
    "int one twenty eight": "Int128",
    "int one hundred and twenty eight": "Int128",
    "you int": "Int8",
    "you int eight": "UInt8",
    "you int sixteen": "UInt16",
    "you int thirty two": "UInt32",
    "you int sixty four": "UInt64",
    "you int one twenty eight": "UInt128",
    "you int one hundred and twenty eight": "UInt128",
    "float": "Float",
    "double": "Double",
    "float sixteen": "Float16",
    "float eighty": "Float80",
    "float thirty two": "Float32",
    "float sixty four": "Float64",
}

other_common_types = {
    "array": "[]",
    "tuple": "()",
    "bool": "Bool",
    "boolean": "Bool",
    "string": "String",
    "char": "Character",
    "character": "Character",
}

common_standard_dictionary_types = {
    **number_types,
    **other_common_types,
}

ctx.lists["user.code_type"] = common_standard_dictionary_types
