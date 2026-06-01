class Scale:
    RAW_NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    NUM_NOTES = 12

    def __init__(self, tonic):
        self._tonic = Note(tonic)
        self._scale_start = self.RAW_NOTES.index(self._tonic.to_sharp())
        self._full_chromatic = self._notes()[self._scale_start:] + self._notes()[:self._scale_start + 1]

    def chromatic(self):
        return self._full_chromatic[:12]

    def interval(self, intervals):
        interval_scale = [self._full_chromatic[0]]
        pointer = 0
        for step in self._stepify(intervals):
            pointer += step
            interval_scale.append(self._full_chromatic[pointer])

        return interval_scale

    def _stepify(self, intervals):
        steps = []
        for interval in intervals:
            if interval == 'M':
                steps.append(2)
            if interval == 'm':
                steps.append(1)
            if interval == 'A':
                steps.append(3)

        return steps


    def _notes(self):
        return [Note(note) for note in self.RAW_NOTES]


class Note:
    EQUIVALENTS = {
        'A#': 'Bb',
        'C#': 'Db',
        'D#': 'Eb',
        'F#': 'Gb',
        'G#': 'Ab',
        'Bb': 'A#',
        'Db': 'C#',
        'Eb': 'D#',
        'Gb': 'F#',
        'Ab': 'G#',
    }

    def __init__(self, string_note):
        self.note = self._standardize(string_note)

    def __eq__(self, string_note):
        return self.note == string_note or self.EQUIVALENTS.get(self.note) == string_note

    def __str__(self):
        return self.note

    def to_sharp(self):
        if len(self.note) == 2 and self.note[1] == 'b':
            return str(self.EQUIVALENTS[self.note])
        return str(self.note)

    def _standardize(self, string_note):
        if len(string_note) == 1:
            return string_note.upper()
        if len(string_note) == 2:
            return string_note[0].upper() + string_note[1]

        raise ValueError(f'{string_note} is not a valid note')

