import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows the difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    return parser.parse_args()
