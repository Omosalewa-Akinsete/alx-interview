#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    # Number of bytes to be processed in the current UTF-8 character
    num_bytes = 0

    # Masks to check the first few bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1's
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            # For 1-byte characters
            if num_bytes == 0:
                continue

            # Invalid scenarios according to UTF-8 rules
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is of the form 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the number of bytes to be processed
        num_bytes -= 1

    # All characters must be processed correctly
    return num_bytes == 0
