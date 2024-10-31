#!/usr/bin/python3
"""Module for parsing HTTP logs."""
import re
from typing import Dict, Match, Tuple, TypedDict


class LogInfo(TypedDict):
    """Type definition for log information dictionary."""
    status_code: str
    file_size: int


def extract_input(line: str) -> LogInfo:
    """Extracts sections of a line of an HTTP request log.

    Args:
        line (str): The line to parse from the log file.

    Returns:
        LogInfo: Dictionary containing the status code and file size.
    """
    pattern: Tuple[str, str, str, str, str] = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info: LogInfo = {
        'status_code': '0',
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(
        pattern[0], pattern[1], pattern[2], pattern[3], pattern[4])
    resp_match: Match[str] | None = re.fullmatch(log_fmt, line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size: int,
                     status_codes_stats: Dict[str, int]) -> None:
    """Print the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): Total size of all files processed.
        status_codes_stats (Dict[str, int]): Dictionary of status code counts.
    """
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line: str, total_file_size: int,
                   status_codes_stats: Dict[str, int]) -> int:
    """Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): Current total file size.
        status_codes_stats (Dict[str, int]): Dictionary of status code counts.

    Returns:
        int: The new total file size.
    """
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run() -> None:
    """Starts the log parser.

    Reads input line by line, updating metrics and printing statistics
    every 10 lines or when interrupted.
    """
    line_num = 0
    total_file_size = 0
    status_codes_stats: Dict[str, int] = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
