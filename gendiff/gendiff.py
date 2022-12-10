from gendiff.formatters import stylish, json, plain
from . import read_data
from .compose_diff_list import compose_diff_list
from .convert_files_to_dict import convert_file_data_to_dict
from .utilities import format_nones_and_bools

formatters = {
    "stylish": lambda diff: stylish.format_as_stylish(diff),
    "plain": lambda diff: plain.format_as_plain(diff),
    "json": lambda diff: json.format_as_json(diff),
}


def generate_diff(
    file1_path: str, file2_path: str, format_name="stylish"
) -> str:
    file1_data, file2_data = read_data.read_files_from_disk(
        file1_path, file2_path
    )
    if file1_path.split(".")[1] == file2_path.split(".")[1] == "yml":
        items_1, items_2 = convert_file_data_to_dict(
            file1_data, file2_data, "yml"
        )
    elif file1_path.split(".")[1] == file2_path.split(".")[1] == "json":
        items_1, items_2 = convert_file_data_to_dict(
            file1_data, file2_data, "json"
        )
    else:
        raise Exception(
            """File extension is not supported or files has extensions
            that aren't the same, both files should have .json or .yml
            extensions."""
        )
    diff = compose_diff_list(
        format_nones_and_bools(items_1), format_nones_and_bools(items_2)
    )
    return formatters[format_name](diff)
