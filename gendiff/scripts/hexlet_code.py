#!/usr/bin/env python3

from gendiff import setup_argument_parser
from gendiff import deserialize_files_to_dict, generate_diff
from gendiff.formatters import stylish, plain, json_formatter


def main():
    parser = setup_argument_parser()
    args = parser.parse_args()
    dicts = deserialize_files_to_dict(args.first_file, args.second_file)
    diff = generate_diff(*dicts)
    formatted_diff = None
    if args.format == "stylish":
        formatted_diff = stylish(diff)
    if args.format == "plain":
        formatted_diff = plain(diff)
    if args.format == "json":
        formatted_diff = json_formatter(diff)
    print(formatted_diff)


if __name__ == "__main__":
    main()
