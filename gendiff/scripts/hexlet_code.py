#!/usr/bin/env python3

from ..cli import parse_args
from ..gendiff import generate_diff
from gendiff import deserialize_files_to_dict


def main():
    parsed = parse_args()
    dicts = deserialize_files_to_dict(parsed.first_file, parsed.second_file)
    result = generate_diff(*dicts)
    print(result)


if __name__ == "__main__":
    main()
