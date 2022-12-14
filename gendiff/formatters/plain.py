from collections.abc import Iterable
from numbers import Number
from .. import compose_diff_list


def flatten(nested_list: Iterable) -> any:
    """
    Yields values from arbitrarily nested list
    :param nested_list: nested list to yield values from
    :return: a value from a list
    """
    for x in nested_list:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


def format_value(input_value: any) -> str:
    """
    Formats value for use with plain formatter
    :param input_value: value to be formatted
    :return: formatted string
    """
    if isinstance(input_value, (list, dict)):
        result = "[complex value]"
    elif isinstance(input_value, Number):
        result = str(input_value)
    elif input_value in ("true", "false", "null"):
        result = input_value
    else:
        result = f"'{input_value}'"

    return result


def generate_diff_line(node: dict, path: str) -> str:
    """
    Returns string representation of a node
    :param node:
    :param path:
    :return:
    """
    result = None
    presence_status = compose_diff_list.get_presence_status(node)
    value = format_value(compose_diff_list.get_value(node))
    old_value = (
        format_value(compose_diff_list.get_old_value(node))
        if presence_status == "updated"
        else None
    )
    if presence_status == "added":
        result = f"Property '{path}' was added with value: {value}"
    if presence_status == "removed":
        result = f"Property '{path}' was removed"
    if presence_status == "updated":
        result = f"Property '{path}' was updated. From {old_value} to {value}"
    return result


def format_node_recursively(diff_node: dict) -> map | str:
    """
    Formats node with all its children
    :param diff_node: node from difference generated by gendiff/gendiff.py
    :return: returns str or map object
    """

    def inner(node, path=""):
        name = compose_diff_list.get_name(node)
        status = compose_diff_list.get_presence_status(node)
        value = compose_diff_list.get_value(node)
        curr_path = path + "." + name if len(path) > 0 else name
        # TODO fix this
        if status != "both":
            return generate_diff_line(node, curr_path)
        if compose_diff_list.has_children(value):
            return map(lambda _node: inner(_node, curr_path), value)

    return inner(diff_node)


def format_as_plain(diff: list) -> str:
    """
    Formats difference in plain textual style
    :param diff: difference between two dicts generated by gendiff/gendiff.py
    :return: string that represents the difference
    """
    diff_formatted = map(format_node_recursively, diff)
    flattened_and_filtered = filter(
        lambda el: el is not None, flatten(diff_formatted)
    )
    return "\n".join(flattened_and_filtered)
