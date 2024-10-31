#!/usr/bin/python3
"""Module for log parsing"""
import sys
import re
from typing import Dict, Match


def print_statistics(total_size: int, status_codes: Dict[int, int]) -> None:
    """
    Print the current statistics of total file size and
        status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line: str) -> Match:
    """Parse a log line using regex and return the match object."""
    pattern = (
        r'^'
        r'(\d+\.\d+\.\d+\.\d+)'
        r'\s-\s'
        r'\['
        r'(.*?)'
        r'\]\s'
        r'"GET /projects/260 HTTP/1.1"\s'
        r'(\d+)'
        r'\s'
        r'(\d+)'
        r'$'
    )
    return re.match(pattern, line)


def main():
    """Main function to process log lines and compute metrics."""
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0}

    try:
        for line in sys.stdin:
            try:
                match = parse_line(line.strip())
                if match:
                    status_code = int(match.group(3))
                    file_size = int(match.group(4))

                    if status_code in status_codes:
                        status_codes[status_code] += 1
                    total_size += file_size
                    line_count += 1

                    if line_count % 10 == 0:
                        print_statistics(total_size, status_codes)

            except (ValueError, EOFError):
                continue

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
