#!/usr/bin/env python3

from gendiff import convert_files_to_dict, generate_diff
from gendiff import setup_argument_parser


def main():
    parser = setup_argument_parser()
    args = parser.parse_args()
    format_name = args.format
    diff = generate_diff(
        args.first_file_path, args.second_file_path, format_name
    )
    print(diff)


if __name__ == "__main__":
    main()
