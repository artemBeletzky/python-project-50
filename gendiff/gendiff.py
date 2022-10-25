class MissingNode:
    def __init__(self):
        self.value = None


def is_leaf(node) -> bool:
    return node["is_leaf"] is True


def has_children(node):
    return node["is_leaf"] is True and len(node["children"]) > 0


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


def generate_diff(items_1: dict, items_2: dict):
    missing_node = MissingNode()

    def inner(node_1, node_2):
        sorted_set_of_keys = sorted({*dict.keys(node_1), *dict.keys(node_2)})
        result = []
        for key in sorted_set_of_keys:
            node_1_value, node_2_value = node_1.get(
                key, missing_node
            ), node_2.get(key, missing_node)
            if (
                node_1_value is not missing_node
                and node_2_value is not missing_node
            ):
                if isinstance(node_1_value, dict) and isinstance(
                    node_2_value, dict
                ):
                    result.append(
                        {
                            "node_name": key,
                            "status": "both",
                            "is_leaf": False,
                            "children": [*inner(node_1_value, node_2_value)],
                        }
                    )
                    continue
                if node_1_value == node_2_value:
                    result.append(
                        {
                            "node_name": key,
                            "value": node_1_value,
                            "status": "both",
                            "is_leaf": True,
                        }
                    )
                    continue
                if node_1_value != node_2_value:
                    result.append(
                        {
                            "node_name": key,
                            "old_value": node_1_value,
                            "value": node_2_value,
                            "status": "updated",
                            "is_leaf": True,
                        }
                    )
                    continue
            if node_1_value is missing_node:
                result.append(
                    {
                        "node_name": key,
                        "value": node_2_value,
                        "status": "new",
                        "is_leaf": True,
                    }
                )
                continue
            if node_2_value is missing_node:
                result.append(
                    {
                        "node_name": key,
                        "value": node_1_value,
                        "status": "missing_node",
                        "is_leaf": True,
                    }
                )
                continue

        return result

    return inner(items_1, items_2)
