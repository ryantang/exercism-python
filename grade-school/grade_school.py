class School:
    def __init__(self):
        self._roster = []
        self._added = []

    def add_student(self, name, grade):
        if self._roster_contains(name):
            self._added.append(False)
        else:
            self._roster.append({"name": name, "grade": grade})
            self._added.append(True)
            self._roster.sort(key=lambda s: (s["grade"], s["name"]))

    def roster(self):
        return [
            student["name"]
            for student in self._roster
        ]

    def grade(self, grade_number):
        return [
            student["name"]
            for student in self._roster
            if student["grade"] == grade_number
        ]

    def added(self):
        return self._added

    def _roster_contains(self, name):
        return any(student_name == name for student_name in self.roster())