"""Build musical scales from a tonic, as chromatic or interval-based sequences."""

from itertools import accumulate


class Scale:
    """Generate chromatic and interval-based scales from a tonic."""

    SHARP = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    FLAT = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    SHARP_SIG = {'G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#'}
    # Keys that use flats: 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb'
    NATURAL_SIG = {'C', 'a'}
    NUM_NOTES = 12
    INTERVALS = {'m': 1, 'M': 2, 'A': 3}

    def __init__(self, tonic: str) -> None:
        self._scale = self.SHARP if tonic in (self.SHARP_SIG | self.NATURAL_SIG) else self.FLAT
        self._scale_start = self._scale.index(self._normalize(tonic))
        self._full_chromatic = self._scale[self._scale_start:] + self._scale[:self._scale_start + 1]

    def chromatic(self) -> list[str]:
        """Return the 12-note chromatic scale starting from the tonic."""
        return self._full_chromatic[:self.NUM_NOTES]

    def interval(self, intervals: list[str]) -> list[str]:
        """Return the scale's notes selected by interval steps (m/M/A)."""
        steps = [self.INTERVALS[interval] for interval in intervals]

        return [
            self._full_chromatic[index]
            for index in accumulate(steps, initial=0)
        ]

    @staticmethod
    def _normalize(note: str) -> str:
        """Capitalize a note's letter, leaving any accidental intact."""
        if not 1 <= len(note) <= 2:
            raise ValueError(f'{note} is not a valid note')

        return note[0].upper() + note[1:]
