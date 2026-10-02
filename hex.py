#!/usr/bin/env python3
"""Quick conversions between hex, ASCII, decimal and binary."""

import sys


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: python3 hex.py [ascii|hex|dec|bin] VALUE", file=sys.stderr)
        return 1
    mode, value = sys.argv[1].lower(), sys.argv[2]

    if mode == "ascii":
        print("hex:", value.encode().hex())
    elif mode == "hex":
        try:
            print("ascii:", bytes.fromhex(value).decode(errors="replace"))
            print("dec:", int(value, 16))
            print("bin:", bin(int(value, 16)))
        except ValueError:
            print("invalid hex value", file=sys.stderr)
            return 1
    elif mode == "dec":
        print("hex:", hex(int(value)))
        print("bin:", bin(int(value)))
    elif mode == "bin":
        print("hex:", hex(int(value, 2)))
        print("dec:", int(value, 2))
    else:
        print(f"unknown mode: {mode}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
