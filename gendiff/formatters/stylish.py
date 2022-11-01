import json
from gendiff import gendiff


# TODO какие методы используются при работе с diff?

def format_node(node: dict) -> str:
    key = gendiff.get_name(node)
    value = gendiff.get_value(node)
    old_value = (
        gendiff.get_old_value(node)
        if gendiff.get_status(node) == "updated"
        else None
    )
    # value_formatted = value if isinstance(value, str) else json.dumps(value)
    # old_value_formatted = old_value if isinstance(old_value, str) else json.dumps(old_value)
    value_formatted = json.dumps(value, indent="\t")
    old_value_formatted = json.dumps(old_value, indent="\t")
    if gendiff.is_leaf(node):
        if gendiff.get_status(node) == "missing_node":
            return "\t" + "".join(("- ", f"{key}", ": ", value_formatted)) + "\n"
        if gendiff.get_status(node) == "both":
            return "\t" + "".join(("  ", f"{key}", ": ", value_formatted)) + "\n"
        if gendiff.get_status(node) == "new":
            return "\t" + "".join(("+ ", f"{key}", ": ", value_formatted)) + "\n"
        if gendiff.get_status(node) == "updated":
            return (
                    "\t" + "".join(("- ", f"{key}", ": ", old_value_formatted))
                    + "\n\t"
                    + "\t" + "".join(("+ ", f"{key}", ": ", value_formatted, "\n"))
            )


def format_diff_stylish(diff: list) -> str:
    result = ""
    for node in diff:
        if not gendiff.is_leaf(node):
            result += f"\t{gendiff.get_name(node)}: {format_diff_stylish(gendiff.get_children(node))}"
        else:
            result += "\t" + format_node(node)
    return f"{{\n{result}}}\n"
