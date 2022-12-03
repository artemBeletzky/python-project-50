from gendiff import convert_files_to_dict
from gendiff.formatters import (
    format_as_json,
    format_as_stylish,
    format_as_plain,
)


def has_children(node: dict) -> bool:
    return node.get("children") is not None


def get_children(node):
    return node["children"]


def get_value(node):
    return node["value"]


def get_old_value(node):
    return node["old_value"]


def get_status(node):
    return node["status"]


def get_name(node):
    return node["node_name"]


def create_node_with_children(node_name: str, status: str, children: list):
    return {"node_name": node_name, "status": status, "children": children}


def create_node_without_children(
    node_name: str, status: str, value: any, **additional_values
):
    node = {"node_name": node_name, "status": status, "value": value}
    if "old_value" in additional_values:
        node["old_value"] = additional_values["old_value"]

    return node


def inner(node_1, node_2) -> list:
    sorted_set_of_keys = sorted({*dict.keys(node_1), *dict.keys(node_2)})
    result = []
    for key in sorted_set_of_keys:
        node_1_value, node_2_value = node_1.get(key, "not found"), node_2.get(
            key, "not found"
        )
        if "not found" not in (node_1_value, node_2_value):
            if isinstance(node_1_value, dict) and isinstance(
                node_2_value, dict
            ):
                children = [*inner(node_1_value, node_2_value)]
                node = create_node_with_children(
                    node_name=key, status="both", children=children
                )
                result.append(node)
            elif node_1_value == node_2_value:
                node = create_node_without_children(
                    node_name=key, status="both", value=node_1_value
                )
                result.append(node)
            elif node_1_value != node_2_value:
                node = create_node_without_children(
                    node_name=key,
                    status="updated",
                    value=node_2_value,
                    old_value=node_1_value,
                )
                result.append(node)
        if node_1_value == "not found":
            if isinstance(node_2_value, dict):
                children = [*inner({}, node_2_value)]
                node = create_node_with_children(
                    node_name=key, status="new", children=children
                )
                result.append(node)
            else:
                node = create_node_without_children(
                    node_name=key, status="new", value=node_2_value
                )
                result.append(node)
        if node_2_value == "not found":
            node = create_node_without_children(
                node_name=key, status="removed", value=node_1_value
            )
            result.append(node)
    return result


def generate_diff(
    file_1_path: str, file_2_path: str, format_name="stylish"
) -> str:
    items_1, items_2 = convert_files_to_dict(file_1_path, file_2_path)
    diff = inner(items_1, items_2)
    print("diff:", diff)
    if format_name == "stylish":
        formatted_diff = format_as_stylish(diff)
    if format_name == "plain":
        formatted_diff = format_as_plain(diff)
    if format_name == "json":
        formatted_diff = format_as_json(diff)
    return formatted_diff
