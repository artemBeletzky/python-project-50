import json
import pathlib
from functools import reduce


# def generate_diff(dict_1, dict_2) -> str:
#     unique_keys = sorted({*dict.keys(dict_1), *dict.keys(dict_2)})
#     content = []
#
#     for key in unique_keys:
#         dict_1_value, dict_2_value = dict_1.get(key), dict_2.get(key)
#         dict_1_value_serialized = (
#             json.dumps(dict_1_value)
#             if type(dict_1_value) is not str
#             else dict_1_value
#         )
#         dict_2_value_serialized = (
#             json.dumps(dict_2_value)
#             if type(dict_2_value) is not str
#             else dict_2_value
#         )
#         if dict_1_value and dict_2_value:
#             if dict_1_value == dict_2_value:
#                 content.append(
#                     "".join(("    ", f"{key}", ": ", dict_1_value_serialized))
#                 )
#             else:
#                 content.append(
#                     "".join(("  - ", f"{key}", ": ", dict_1_value_serialized))
#                 )
#                 content.append(
#                     "".join(("  + ", f"{key}", ": ", dict_2_value_serialized))
#                 )
#         if dict_2_value is None:
#             content.append(
#                 "".join(("  - ", f"{key}", ": ", dict_1_value_serialized))
#             )
#         if dict_1_value is None:
#             content.append(
#                 "".join(("  + ", f"{key}", ": ", dict_2_value_serialized))
#             )
#
#     joined_lines = "\n".join(content)
#     return f"{{\n{joined_lines}\n}}"
#
#
# print(generate_diff(dic_1, dic_2))


# def foo(dict_1, dict_2):
#     def inner(keys):
#         for key in keys:
#             if type(dic_1[key]) is dict:
#                 print("IT'S A DICT!")
#                 return inner(dic_1[key])
#             print(key)
#
#     return inner(sorted({*dict.keys(dict_1), *dict.keys(dict_2)}))
#
#
# foo(dic_1, dic_2)


def is_leaf() -> bool:
    pass


def has_children():
    pass


def get_children():
    pass


def get_name():
    pass


file_1_path = pathlib.Path.cwd().joinpath("tests/fixtures/file1_nested.json")
file_2_path = pathlib.Path.cwd().joinpath("tests/fixtures/file2_nested.json")

with open(file_1_path, "r") as file_1, open(file_2_path, "r") as file_2:
    file_1_dict, file_2_dict = json.load(file_1), json.load(file_2)


# print(file_1_dict)
# print(json.dumps(file_1_dict))

# TODO create types for nodes
# TODO create functions that will help to create nodes


def create_node(node):
    if is_leaf():
        pass


def check_status(node_1, node_2, key):
    pass


class Null:
    def __init__(self):
        pass


null = Null()


def generate_diff(items_1: dict, items_2: dict):
    def inner(node_1, node_2):
        sorted_set_of_keys = sorted({*dict.keys(node_1), *dict.keys(node_2)})
        result = []
        for key in sorted_set_of_keys:
            node_1_value, node_2_value = node_1.get(key, null), node_2.get(key, null)
            if node_1_value is not null and node_2_value is not null:
                if isinstance(node_1_value, dict) and isinstance(node_2_value, dict):
                    result.append(
                        {
                            "node_name": key,
                            "status": "both",
                            "is_leaf": False,
                            "children": [*inner(node_1_value, node_2_value)],
                        })
                if node_1_value == node_2_value:
                    result.append(
                        {
                            "node_name": key,
                            "value": node_1_value,
                            "status": "both",
                            "is_leaf": True,
                        }
                    )
                if node_1_value != node_2_value:
                    result.append(
                        {
                            "node_name": key,
                            "old_value": node_1_value,
                            "value": node_2_value,
                            "status": "updated",
                            "is_leaf": True,
                        }
                    )
            if node_1_value is null:
                if isinstance(node_2_value, dict):
                    result.append(
                        {
                            "node_name": key,
                            "status": "new",
                            "is_leaf": False,
                            "children": [*inner({}, node_2_value)],
                        }
                    )
                else:
                    result.append(
                        {
                            "node_name": key,
                            "value": node_2_value,
                            "status": "new",
                            "is_leaf": True,
                        }
                    )
            if node_2_value is null:
                if isinstance(node_1_value, dict):
                    result.append(
                        {
                            "node_name": key,
                            "status": "missing",
                            "is_leaf": False,
                            "children": [*inner(node_1_value, {})],
                        }
                    )
                else:
                    result.append(
                        {
                            "node_name": key,
                            "value": node_1_value,
                            "status": "missing",
                            "is_leaf": True,
                        }
                    )

        return result

    return inner(items_1, items_2)


print(generate_diff(file_1_dict, file_2_dict))
