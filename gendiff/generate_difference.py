def has_children(value) -> bool:
    """Receives value from node returns 'true' if this value contains children"""
    return type(value) == list


def get_value(node: dict) -> any:
    return node["value"]


def get_old_value(node: dict) -> [None, any]:
    return node.get("old_value")


def get_presence_status(node: dict) -> str:
    return node["presence_status"]


def get_name(node: dict) -> str:
    return node["name"]


def traverse(i1: dict, i2: dict) -> list:
    res = []
    for key in sorted({*i1.keys(), *i2.keys()}):
        val1, val2 = i1.get(key), i2.get(key)
        if val1 is not None and val2 is not None:
            if type(val1) == type(val2) == dict:
                res.append(
                    {
                        "name": key,
                        "presence_status": "both",
                        "value": traverse(val1, val2),
                    }
                )
            elif val1 == val2:
                val = traverse(val1, val1) if type(val1) == dict else val1
                res.append(
                    {"name": key, "presence_status": "both", "value": val}
                )
            elif val1 != val2:
                curr_val = traverse(val2, val2) if type(val2) == dict else val2
                old_val = traverse(val1, val1) if type(val1) == dict else val1
                res.append(
                    {
                        "name": key,
                        "presence_status": "updated",
                        "value": curr_val,
                        "old_value": old_val,
                    }
                )
        if val2 is None:
            val = traverse(val1, val1) if type(val1) == dict else val1
            res.append(
                {"name": key, "presence_status": "removed", "value": val}
            )
        elif val1 is None:
            val = traverse(val2, val2) if type(val2) == dict else val2
            res.append({"name": key, "presence_status": "added", "value": val})

    return res
