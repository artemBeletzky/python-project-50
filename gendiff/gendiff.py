from .deserialize import convert_files_to_dict
from gendiff.formatters import stylish, json, plain
from .generate_difference import traverse
from .utilities import format_nones_and_bools


def generate_diff(
    file_1_path: str, file_2_path: str, format_name="stylish"
) -> str:
    # TODO it might only need to read it? why is it all together?
    items_1, items_2 = convert_files_to_dict(file_1_path, file_2_path)

    diff = traverse(
        format_nones_and_bools(items_1), format_nones_and_bools(items_2)
    )
    formatted_diff = None

    if format_name == "stylish":
        formatted_diff = stylish.format_as_stylish(diff)
    if format_name == "plain":
        formatted_diff = plain.format_as_plain(diff)
    if format_name == "json":
        formatted_diff = json.format_as_json(diff)
    return formatted_diff
