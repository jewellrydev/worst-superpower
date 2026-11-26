#!/usr/bin/env python3
"""Timezone Man — entry for Worst Superpower on make.fun.

Prints exactly one line (at most 140 characters) inventing the most
useless superpower possible.
"""

LINE = "The power to always know exactly what time it is, but only in a timezone where nobody has ever lived."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 140
    print(LINE)


if __name__ == "__main__":
    main()
