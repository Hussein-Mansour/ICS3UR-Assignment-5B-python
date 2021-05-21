#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Thu/May20/2021
# This program generates the sin table for each degree

import math


def main():
    # this function calculates and print the sing table
    # process  & output
    for counter in range(180 + 1):
        math_sin_start = counter / 180 * math.pi
        math_sin_end = math.sin(math_sin_start)

        math_sin_start = round(math_sin_start, 7)
        math_sin_end = round(math_sin_end, 7)

        if (math_sin_end == 0.0):
            math_sin_end = int(math_sin_end)

        print("Sin({}°) = {}".format(counter, math_sin_end))

    print("\nDone.")


if __name__ == "__main__":
    main()
