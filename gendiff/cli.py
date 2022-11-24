import argparse


def setup_argument_parser():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows the difference."
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        default="stylish",
        help="Specify format of output",
        choices=["stylish", "plain"],
    )
    return parser
