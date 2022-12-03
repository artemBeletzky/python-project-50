import functools
import json
import operator
import re
import gendiff


# TODO Use function from plain formatter
def flatten_nested_list(nested_list) -> list:
    temp_list = []
    for el in nested_list:
        if type(el) is list:
            temp_list.append(el)
        else:
            temp_list.append([el])
    return functools.reduce(operator.iconcat, temp_list, [])


# TODO FIX setting5 indentation!!
def format_node(node) -> list | tuple:
    key = gendiff.get_name(node)
    status = gendiff.get_status(node)
    value = gendiff.get_value(node)
    old_value = gendiff.get_old_value(node) if status == "updated" else None
    if status == "removed":
        return f"- {key}", value
    if status == "both":
        return f"  {key}", value
    if status == "new":
        return f"+ {key}", value
    if status == "updated":
        return [(f"- {key}", old_value), (f"+ {key}", value)]


def format_diff(node: dict) -> tuple | list:
    name = gendiff.get_name(node)
    if not gendiff.has_children(node):
        return format_node(node)
    else:
        children = gendiff.get_children(node)
        children_formatted = list(map(format_diff, children))
        children_flattened = flatten_nested_list(children_formatted)
        return name, dict(children_flattened)


def format_as_stylish(diff: list) -> str:
    diff_formatted = list(map(format_diff, diff))
    json_converted = json.dumps(
        dict(flatten_nested_list(diff_formatted)), indent="  "
    )
    quotes_and_commas_removed = re.sub('[,"]', "", json_converted)
    return quotes_and_commas_removed
