import functools
import json
import operator
import re
import gendiff
import gendiff.generate_diff


# TODO какие методы используются при работе с diff?


# def format_diff_stylish(node: dict):
#     name = gendiff.get_name(node)
#     if gendiff.is_leaf(node):
#         return [] + [(name, gendiff.get_value(node))]


temp_children = [
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
                "status": "missing_node",
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
        "status": "missing_node",
        "is_leaf": True,
    },
    {
        "node_name": "group3",
        "value": {"deep": {"id": {"number": 45}}, "fee": 100500},
        "status": "new",
        "is_leaf": True,
    },
]

flat = [{'node_name': 'follow', 'value': False, 'status': 'missing_node', 'is_leaf': True},
        {'node_name': 'host', 'value': 'hexlet.io', 'status': 'both', 'is_leaf': True},
        {'node_name': 'proxy', 'value': '123.234.53.22', 'status': 'missing_node', 'is_leaf': True},
        {'node_name': 'timeout', 'old_value': 50, 'value': 20, 'status': 'updated', 'is_leaf': True},
        {'node_name': 'verbose', 'value': True, 'status': 'new', 'is_leaf': True}]


def transform(nested_list):
    regular_list = []
    for ele in nested_list:
        if type(ele) is list:
            regular_list.append(ele)
        else:
            regular_list.append([ele])
    return functools.reduce(operator.iconcat, regular_list, [])


def format_node(node):
    key = gendiff.get_name(node)
    status = gendiff.get_status(node)
    value = gendiff.get_value(node)
    old_value = gendiff.get_old_value(node) if status == "updated" else None
    if status == "missing_node":
        return f"-  {key}", value
    if status == "both":
        return f"   {key}", value
    if status == "new":
        return f"+  {key}", value
    if status == "updated":
        return [(f"-  {key}", old_value), (f"+  {key}", value)]


def format_diff(node: dict):
    name = gendiff.get_name(node)
    if gendiff.is_leaf(node):
        val = format_node(node)
        return val
    else:
        children = gendiff.get_children(node)
        test_val = list(map(format_diff, children))
        flattened = transform(test_val)
        return name, dict(flattened)


result = list(map(format_diff, flat))
dict_converted = dict(transform(result))
json_converted = json.dumps(dict_converted, indent='\t')
removed_chars = re.sub("[,\"]", '', json_converted)
print(repr(removed_chars))
