import functools
import json
import operator
from .. import compose_diff_list


# TODO Use function from plain formatter
def flatten_nested_list(nested_list) -> list:
    temp_list = []
    for el in nested_list:
        if type(el) is list:
            temp_list.append(el)
        else:
            temp_list.append([el])
    return functools.reduce(operator.iconcat, temp_list, [])


def format_node(node) -> list | tuple:
    key = compose_diff_list.get_name(node)
    status = compose_diff_list.get_presence_status(node)
    value = compose_diff_list.get_value(node)
    old_value = (
        compose_diff_list.get_old_value(node) if status == "updated" else None
    )
    if status == "removed":
        return "removed", f"{key}: {value}"
    if status == "both":
        return "present in both", f"{key}: {value}"
    if status == "added":
        return "added", f"{key}: {value}"
    if status == "updated":
        return [
            ("removed", f"{key}: {old_value}"),
            ("added", f"{key}: {value}"),
        ]


def format_diff(node: dict) -> tuple | list:
    name = compose_diff_list.get_name(node)
    value = compose_diff_list.get_value(node)
    if not compose_diff_list.has_children(value):
        return format_node(node)
    else:
        children_formatted = list(map(format_diff, value))
        children_flattened = flatten_nested_list(children_formatted)
        return name, dict(children_flattened)


def format_as_json(diff: list) -> str:
    diff_formatted = list(map(format_diff, diff))
    json_converted = json.dumps(
        dict(flatten_nested_list(diff_formatted)), indent="\t"
    )
    return json_converted
