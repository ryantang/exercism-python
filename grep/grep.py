from collections import namedtuple
from dataclasses import dataclass

LineMatch = namedtuple('LineMatch', ['file', 'line_num', 'line'])

@dataclass
class GrepConfig:
    # matching configs
    case_insensitive: bool = False
    invert_match: bool = False
    match_full_line: bool = False

    # output configs
    matching_files_only: bool = False
    show_line_number: bool = False
    show_file_name: bool = False


def grep(pattern: str, flags: str, files: list[str]) -> list[str]:
    config = _parse(flags, len(files))
    results = []

    for file_name in files:
        with open(file_name, 'r') as file_handle:
            for index, line in enumerate(file_handle):
                if _line_match(pattern, config, line):
                    results.append(LineMatch(f'{file_name}\n', line_num=index+1, line=line))

    if config.matching_files_only:
        matching_files = (match.file for match in results)
        return ''.join(list(dict.fromkeys(matching_files)))

    if config.show_file_name and config.show_line_number:
        return ''.join([
            f'{result.file.strip()}:{result.line_num}:{result.line}'
            for result in results
        ])

    if config.show_line_number:
        return ''.join([
            f'{result.line_num}:{result.line}'
            for result in results
        ])

    if config.show_file_name:
        return ''.join([
            f'{result.file.strip()}:{result.line}'
            for result in results
        ])

    return ''.join([
            f'{result.line}'
            for result in results
        ])


def _parse(flags: str, num_files: int) -> GrepConfig:
    config = GrepConfig()
    if '-i' in flags:
        config.case_insensitive = True
    if '-x' in flags:
        config.match_full_line = True
    if '-v' in flags:
        config.invert_match = True

    if '-l' in flags:
        config.matching_files_only = True
    if '-n' in flags:
        config.show_line_number = True
    if num_files > 1:
        config.show_file_name = True

    return config


def _line_match(pattern: str, config: GrepConfig, line: str) -> bool:
    if config.case_insensitive:
        return pattern.lower() in line.lower()

    if config.match_full_line and config.invert_match:
        return pattern != line.strip()

    if config.match_full_line:
        return pattern == line.strip()

    if config.invert_match:
        return pattern not in line

    return pattern in line
