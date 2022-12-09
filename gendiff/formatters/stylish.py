from gendiff import generate_difference

statuses = {"added": "+ ", "removed": "- ", "both": "  "}


# TODO all the functions below should be refactored
def format_node_with_children(key, children, status, spaces_count):
    return f"{' ' * spaces_count}{statuses[status]}{key}: {{\n{''.join(children)}{' ' * (spaces_count + 2)}}}\n"


def format_without_children(name, val, spaces_count, status):
    return f"{' ' * spaces_count}{statuses[status]}{name}: {val}\n"


def format_node(name, val, old_val, status, spaces_count):
    if status == "updated":
        formatted_val = (
            format_node_with_children(
                name, children=val, status="added", spaces_count=spaces_count
            )
            if generate_difference.has_children(val)
            else format_without_children(name, val, spaces_count, "added")
        )
        formatted_old_val = (
            format_node_with_children(
                name,
                children=old_val,
                status="removed",
                spaces_count=spaces_count,
            )
            if generate_difference.has_children(old_val)
            else format_without_children(name, old_val, spaces_count, "removed")
        )
        return formatted_old_val + formatted_val
    else:
        return (
            format_node_with_children(
                name, children=val, status=status, spaces_count=spaces_count
            )
            if generate_difference.has_children(val)
            else format_without_children(name, val, spaces_count, status=status)
        )


def traverse(node, spaces_count=2):
    name = generate_difference.get_name(node)
    _temp_value = generate_difference.get_value(node)
    _temp_old_value = generate_difference.get_old_value(node)
    val = (
        _temp_value
        if not generate_difference.has_children(_temp_value)
        else list(
            map(lambda _node: traverse(_node, spaces_count + 4), _temp_value)
        )
    )
    old_val = (
        _temp_old_value
        if _temp_old_value is None
        or not generate_difference.has_children(_temp_old_value)
        else list(
            map(
                lambda _node: traverse(_node, spaces_count + 4), _temp_old_value
            )
        )
    )
    return format_node(
        name=name,
        val=val,
        old_val=old_val,
        status=generate_difference.get_presence_status(node),
        spaces_count=spaces_count,
    )


def format_as_stylish(diff: list) -> str:
    formatted_diff = map(traverse, diff)
    return f"{{\n{''.join(formatted_diff)}}}"
