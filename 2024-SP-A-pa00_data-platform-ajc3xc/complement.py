#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def complement(seq: str) -> str:
    """
    Purpose:        Converts a DNA sequence to its complement
    Parameters:     Sequence of DNA as a python str
    User Input:     No
    Prints:         Nothing
    Returns:        Result new string of DNA
    Modifies:       Nothing
    Calls:          Basic python only
    Tests:          ./unit_tests/*
    Status:         Done!

    Usage illustrated via some simple doctests:
    >>> complement("GATTACA")
    'CTAATGT'

    >>> complement("CAT")
    'GTA'

    >>> print("Unlike other frameworks, doctest does stdout easily")
    Unlike other frameworks, doctest does stdout easily
    """
    # To debug doctest test in pudb
    # Highlight the line of code below below
    # Type 't' to jump 'to' it
    # Type 's' to 'step' deeper
    # Type 'n' to 'next' over
    # Type 'f' or 'r' to finish/return a function call and go back to caller
    # YOUR CODE GOES HERE
    # A's complement is T, T's complement is A, G's complement is C, C's complement is G
    complement_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join([complement_dict[char] for char in seq])


if __name__ == "__main__":
    # Execute doctests to protect main:
    import doctest

    doctest.testmod()

    # Run main:

    # if not sys.stdin.isatty():
    #    sys.stdin = Tee(input_handle=sys.stdin, output_handle=sys.stdout)
    # input_dna_sequence = input()
    # print(complement(input_dna_sequence))

    # input_dna_sequence = input()
    # print(complement(input_dna_sequence))

    # files were inputted
    if len(sys.argv) == 3:
        import argparse

        parser = argparse.ArgumentParser(description="allow for command line input")
        # Add optional argument with a default value
        parser.add_argument(
            "input_txt_file", type=str, default=None, help="Input Text file"
        )
        parser.add_argument(
            "output_txt_file",
            type=str,
            default=None,
            help="where results should be outputted to",
        )

        # Parse the command line arguments
        args = parser.parse_args()

        # Open the source file in read mode and the target file in write mode
        with open(args.input_txt_file, "r") as input_file, open(
            args.output_txt_file, "w"
        ) as output_file:
            # Read the content from the source file
            for line in input_file:
                input_dna_sequence: str = line.strip()
                inverted_sequence: str = complement(input_dna_sequence)
                output_file.write(inverted_sequence + "\n")
    else:
        input_dna_sequence = input()
        print(complement(input_dna_sequence))
