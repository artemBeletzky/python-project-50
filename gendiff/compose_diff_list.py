def has_children(value: any) -> bool:
    """
    Receives value (or old_value) from a node and returns True if
    this value contains children, returns False otherwise
    """
    return type(value) == list


def get_value(node: dict) -> any:
    return node["value"]


def get_old_value(node: dict) -> [None, any]:
    return node.get("old_value")


def get_presence_status(node: dict) -> str:
    return node["presence_status"]


def get_name(node: dict) -> str:
    return node["name"]


def compose_diff_list(items1: dict, items2: dict) -> list:
    res = []
    for key in sorted({*items1.keys(), *items2.keys()}):
        val1, val2 = items1.get(key), items2.get(key)
        if val1 is not None and val2 is not None:
            if type(val1) == type(val2) == dict:
                res.append(
                    {
                        "name": key,
                        "presence_status": "both",
                        "value": compose_diff_list(val1, val2),
                    }
                )
            elif val1 == val2:
                val = (
                    compose_diff_list(val1, val1)
                    if type(val1) == dict
                    else val1
                )
                res.append(
                    {"name": key, "presence_status": "both", "value": val}
                )
            elif val1 != val2:
                curr_val = (
                    compose_diff_list(val2, val2)
                    if type(val2) == dict
                    else val2
                )
                old_val = (
                    compose_diff_list(val1, val1)
                    if type(val1) == dict
                    else val1
                )
                res.append(
                    {
                        "name": key,
                        "presence_status": "updated",
                        "value": curr_val,
                        "old_value": old_val,
                    }
                )
        if val2 is None:
            val = compose_diff_list(val1, val1) if type(val1) == dict else val1
            res.append(
                {"name": key, "presence_status": "removed", "value": val}
            )
        elif val1 is None:
            val = compose_diff_list(val2, val2) if type(val2) == dict else val2
            res.append({"name": key, "presence_status": "added", "value": val})

    return res
