def choose_value(value):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return "true" if value else "false"
    else:
        return value


def format_nones_and_bools(obj: dict) -> dict:
    """
    Returns new dict which has None values replaced with 'null'
    and bool values replaced with either 'true' or 'false'
    """
    return (
        {k: format_nones_and_bools(choose_value(v)) for k, v in obj.items()}
        if isinstance(obj, dict)
        else obj
    )
