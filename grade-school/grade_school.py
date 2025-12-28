class School:
    def __init__(self):
        self._roster = []
        self._added = []

    def add_student(self, name: str, grade: int) -> None:
        """Add a student to the school roster.
        
        Args:
            name: The student's name
            grade: The grade level (as an integer)
            
        Note:
            If a student with the same name already exists, the student
            is not added. The roster is kept sorted by grade, then by name.
        """
        if self._roster_contains(name):
            self._added.append(False)
        else:
            self._roster.append({"name": name, "grade": grade})
            self._added.append(True)
            self._roster.sort(key=lambda s: (s["grade"], s["name"]))

    def roster(self) -> list[str]:
        """Get all student names in the school.
        
        Returns:
            A list of all student names, sorted by grade level first,
            then alphabetically by name within each grade.
        """
        return [
            student["name"]
            for student in self._roster
        ]

    def grade(self, grade_number: int) -> list[str]:
        """Get all student names in a specific grade.
        
        Args:
            grade_number: The grade level to filter by
            
        Returns:
            A list of student names in the specified grade,
            sorted alphabetically by name.
        """
        return [
            student["name"]
            for student in self._roster
            if student["grade"] == grade_number
        ]

    def added(self) -> list[bool]:
        return self._added

    def _roster_contains(self, name) -> bool:
        return any(student["name"] == name for student in self._roster)