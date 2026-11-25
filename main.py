#!/usr/bin/env python3
"""Fridge Roast entry: writes one roast line to /output/entry.txt.

The line (90 bytes, no trailing newline):
    My smart fridge updated its firmware overnight and now the ice maker only makes apologies.
"""
import argparse
import os

LINE = "My smart fridge updated its firmware overnight and now the ice maker only makes apologies."


def check():
    """Validate the line against the gate without writing anything."""
    data = LINE.encode("utf-8")
    assert 1 <= len(data) <= 200, "entry must be 1-200 bytes"
    assert data.strip() == data, "entry must not be only whitespace"
    assert b"fridge" in data.lower(), "roast must be about a fridge"
    print("check OK (%d bytes)" % len(data))
    return data


def self_test():
    """Write the entry, then read it back and verify it byte for byte."""
    data = check()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch"
    print("self-test PASS: /output/entry.txt is byte-exact (%d bytes)" % len(data))


def main():
    parser = argparse.ArgumentParser(description="Fridge Roast entry")
    parser.add_argument("--check", action="store_true",
                        help="validate the line without writing")
    parser.add_argument("--self-test", action="store_true",
                        help="write the entry and verify it byte for byte")
    args = parser.parse_args()
    if args.check:
        check()
    elif args.self_test:
        self_test()
    else:
        self_test()


if __name__ == "__main__":
    main()
