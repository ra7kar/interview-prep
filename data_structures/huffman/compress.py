#!/usr/bin/env python3

import argparse

from huffman_tree import HuffmanTree

def parse_args():
    """Parse arguments for Huffman tree compression."""
    parser = argparse.ArgumentParser(description='Huffman tree compression')
    parser.add_argument('-i', '--input', 
                        type=str,
                        required=True,
                        help='Input file to perform action on.')
    parser.add_argument('-o', '--output',
                        type=str,
                        required=True,
                        help='Output file to store.')
    parser.add_argument('-a', '--action', 
                        type=str,
                        required=True,
                        choices=['compress', 'decompress'],
                        help='Action to perform on input file.')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    ht = HuffmanTree(args.input, args.output, args.action)

    if args.action == "compress":
        ht.compress()
    else:
        ht.decompress()