#!/usr/bin/env python

import sys

# Input comes from standard input
for line in sys.stdin:
    line = line.strip()
    values = line.split()

    # Process each value in the line
    for value in values:
        try:
            # Convert the value to a float (assuming it's numeric)
            numeric_value = float(value)
            # Emit the numeric value as the key with a count of 1
            print(f"{numeric_value}\t1")
        except ValueError:
            # Non-numeric value; ignore it

