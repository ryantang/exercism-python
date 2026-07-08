from collections import namedtuple

LineMatch = namedtuple('LineMatch', ['file', 'line_num', 'line'])

def grep(pattern, flags, files):
    results = []

    for file_name in files:
        with open(file_name, 'r') as file_handle:
            for index, line in enumerate(file_handle):
                if _line_match(pattern, flags, line):
                    results.append(LineMatch(f'{file_name}\n', line_num=index+1, line=line))

    if '-l' in flags:
        matching_files = (match.file for match in results)
        return ''.join(list(set(matching_files)))

    if len(files) > 1 and '-n' in flags:
        return ''.join([
            f'{result.file.strip()}:{result.line_num}:{result.line}'
            for result in results
        ])

    if '-n' in flags:
        return ''.join([
            f'{result.line_num}:{result.line}'
            for result in results
        ])

    if len(files) > 1:
        return ''.join([
            f'{result.file.strip()}:{result.line}'
            for result in results
        ])

    return ''.join([
            f'{result.line}'
            for result in results
        ])


def _line_match(pattern, flags, line) -> bool:
    if '-i' in flags:
        return pattern.lower() in line.lower()

    if '-x' in flags and '-v' in flags:
        return pattern != line.strip()

    if '-x' in flags:
        return pattern == line.strip()

    if '-v' in flags:
        return pattern not in line

    return pattern in line
