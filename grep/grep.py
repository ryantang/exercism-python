from dataclasses import dataclass


@dataclass
class GrepConfig:
    """Parsed grep options controlling matching and output behavior."""

    # matching configs
    case_insensitive: bool = False
    invert_match: bool = False
    match_full_line: bool = False

    # output configs
    matching_files_only: bool = False
    show_line_number: bool = False
    show_file_name: bool = False


@dataclass
class LineMatch:
    """A single matching line, with its source file and 1-based line number."""

    file: str
    line_num: int
    line: str


def grep(pattern: str, flags: str, files: list[str]) -> str:
    """Search ``files`` for ``pattern`` and return matches formatted per ``flags``."""
    config = _parse(flags)
    results = []

    for file_name in files:
        with open(file_name, encoding='utf-8') as file_handle:
            for index, line in enumerate(file_handle):
                if _line_match(pattern, config, line):
                    results.append(LineMatch(f'{file_name}\n', line_num=index+1, line=line))

    if config.matching_files_only:
        matching_files = (match.file for match in results)
        formatted_results = list(dict.fromkeys(matching_files))
    elif len(files) > 1 and config.show_line_number:
        formatted_results = [
            f'{result.file.strip()}:{result.line_num}:{result.line}'
            for result in results
        ]
    elif config.show_line_number:
        formatted_results = [f'{result.line_num}:{result.line}' for result in results]
    elif len(files) > 1:
        formatted_results = [f'{result.file.strip()}:{result.line}' for result in results]
    else:
        formatted_results = [result.line for result in results]

    return ''.join(formatted_results)


def _parse(flags: str) -> GrepConfig:
    """Convert a flags string (e.g. ``"-i -n"``) into a :class:`GrepConfig`."""
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

    return config


def _line_match(pattern: str, config: GrepConfig, line: str) -> bool:
    """Return True if ``line`` should be included, per matching flags in ``config``."""
    if config.case_insensitive and config.invert_match and config.match_full_line:
        return pattern.lower() != line.lower().strip()

    if config.case_insensitive and config.invert_match:
        return pattern.lower() not in line.lower()

    if config.case_insensitive and config.match_full_line:
        return pattern.lower() == line.lower().strip()

    if config.match_full_line and config.invert_match:
        return pattern != line.strip()

    if config.match_full_line:
        return pattern == line.strip()

    if config.case_insensitive:
        return pattern.lower() in line.lower()

    if config.invert_match:
        return pattern not in line

    return pattern in line
