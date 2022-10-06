import json


def generate_diff(dict_1, dict_2) -> str:
    unique_keys = sorted({*dict.keys(dict_1), *dict.keys(dict_2)})
    content = []

    for key in unique_keys:
        dict_1_value, dict_2_value = dict_1.get(key), dict_2.get(key)
        dict_1_value_serialized = (
            json.dumps(dict_1_value)
            if type(dict_1_value) is not str
            else dict_1_value
        )
        dict_2_value_serialized = (
            json.dumps(dict_2_value)
            if type(dict_2_value) is not str
            else dict_2_value
        )
        if dict_1_value and dict_2_value:
            if dict_1_value == dict_2_value:
                content.append(
                    "".join(("    ", f"{key}", ": ", dict_1_value_serialized))
                )
            else:
                content.append(
                    "".join(("  - ", f"{key}", ": ", dict_1_value_serialized))
                )
                content.append(
                    "".join(("  + ", f"{key}", ": ", dict_2_value_serialized))
                )
        if dict_2_value is None:
            content.append(
                "".join(("  - ", f"{key}", ": ", dict_1_value_serialized))
            )
        if dict_1_value is None:
            content.append(
                "".join(("  + ", f"{key}", ": ", dict_2_value_serialized))
            )

    joined_lines = "\n".join(content)
    return f"{{\n{joined_lines}\n}}"
