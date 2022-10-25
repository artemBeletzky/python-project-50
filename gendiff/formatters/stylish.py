import functools
import json

from gendiff import gendiff

flat = [
    {
        "node_name": "follow",
        "value": False,
        "status": "missing",
        "is_leaf": True,
    },
    {
        "node_name": "host",
        "value": "hexlet.io",
        "status": "both",
        "is_leaf": True,
    },
    {
        "node_name": "proxy",
        "value": "123.234.53.22",
        "status": "missing",
        "is_leaf": True,
    },
    {
        "node_name": "timeout",
        "old_value": 50,
        "value": 20,
        "status": "updated",
        "is_leaf": True,
    },
    {"node_name": "verbose", "value": True, "status": "new", "is_leaf": True},
]

nested_diff = [
    {
        "node_name": "common",
        "status": "both",
        "is_leaf": False,
        "children": [
            {
                "node_name": "follow",
                "value": False,
                "status": "new",
                "is_leaf": True,
            },
            {
                "node_name": "setting1",
                "value": "Value 1",
                "status": "both",
                "is_leaf": True,
            },
            {
                "node_name": "setting2",
                "value": 200,
                "status": "missing",
                "is_leaf": True,
            },
            {
                "node_name": "setting3",
                "old_value": True,
                "value": None,
                "status": "updated",
                "is_leaf": True,
            },
            {
                "node_name": "setting4",
                "value": "blah blah",
                "status": "new",
                "is_leaf": True,
            },
            {
                "node_name": "setting5",
                "value": {"key5": "value5"},
                "status": "new",
                "is_leaf": True,
            },
            {
                "node_name": "setting6",
                "status": "both",
                "is_leaf": False,
                "children": [
                    {
                        "node_name": "doge",
                        "status": "both",
                        "is_leaf": False,
                        "children": [
                            {
                                "node_name": "wow",
                                "old_value": "",
                                "value": "so much",
                                "status": "updated",
                                "is_leaf": True,
                            }
                        ],
                    },
                    {
                        "node_name": "key",
                        "value": "value",
                        "status": "both",
                        "is_leaf": True,
                    },
                    {
                        "node_name": "ops",
                        "value": "vops",
                        "status": "new",
                        "is_leaf": True,
                    },
                ],
            },
        ],
    },
    {
        "node_name": "group1",
        "status": "both",
        "is_leaf": False,
        "children": [
            {
                "node_name": "baz",
                "old_value": "bas",
                "value": "bars",
                "status": "updated",
                "is_leaf": True,
            },
            {
                "node_name": "foo",
                "value": "bar",
                "status": "both",
                "is_leaf": True,
            },
            {
                "node_name": "nest",
                "old_value": {"key": "value"},
                "value": "str",
                "status": "updated",
                "is_leaf": True,
            },
        ],
    },
    {
        "node_name": "group2",
        "value": {"abc": 12345, "deep": {"id": 45}},
        "status": "missing",
        "is_leaf": True,
    },
    {
        "node_name": "group3",
        "value": {"deep": {"id": {"number": 45}}, "fee": 100500},
        "status": "new",
        "is_leaf": True,
    },
]


def format_node(node: dict) -> str:
    key = gendiff.get_name(node)
    value = json.dumps(gendiff.get_value(node))
    old_value = (
        json.dumps(gendiff.get_old_value(node))
        if gendiff.get_status(node) == "updated"
        else None
    )
    if gendiff.is_leaf(node):
        if gendiff.get_status(node) == "missing":
            return "".join(("  - ", f"{key}", ": ", value))
        if gendiff.get_status(node) == "both":
            return "".join(("    ", f"{key}", ": ", value))
        if gendiff.get_status(node) == "new":
            return "".join(("  + ", f"{key}", ": ", value))
        if gendiff.get_status(node) == "updated":
            return "".join(("  - ", f"{key}", ": ", old_value)) + "\n" + "".join(("  + ", f"{key}", ": ", value))


# reduce (if it has children) -> return string with the name of parent (+ tab) and recursive reduce children to

def foo(diff):
    for node in diff:
        if gendiff.is_leaf(node):
            print(format_node(node))
        else:
            print(gendiff.get_name(node))
            print(foo(gendiff.get_children(node)))

foo(nested_diff)
# ВЕРНИ ВЫЗОВ ФУНКЦИИ И +


# def foo(diff) -> str:
#     unique_keys = sorted({*dict.keys(dict_1), *dict.keys(dict_2)})
#     content = []
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
