#!/usr/bin/env python3

from gendiff.cli import parse_args
from gendiff import deserialize_files_to_dict, generate_diff
from gendiff.formatters import format_diff_stylish


def main():
    parsed_args = parse_args()
    dicts = deserialize_files_to_dict(
        parsed_args.first_file, parsed_args.second_file
    )
    diff = generate_diff(*dicts)
    result = format_diff_stylish(diff)
    print(result)


if __name__ == "__main__":
    main()
