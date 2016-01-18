#!/usr/bin/python -tt
# Copyright Austin Ellis

# Binary/Decimal Converter. Convers both ways
"""
Converts binary to decimal or decmial to binary
"""
import sys

binary_values = [128, 64, 32, 16, 8, 4, 2, 1]

def dec_to_bin(num):
    """Convert decimal to binary with dec_to_bin() function """
    bin_converted = []
    i = 0
    while i < 8:
        bin_item = binary_values[i]
        if num >= bin_item:
            bin_converted.append("1")
            num = num - bin_item
            i += 1

        elif num < bin_item:
            bin_converted.append("0")
            i += 1

    return bin_converted

def main():
    converted = dec_to_bin(int(sys.argv[1]))
    print '  '.join(converted)

if __name__ == '__main__':
    main()
