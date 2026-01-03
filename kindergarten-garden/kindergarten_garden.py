class Garden:
    PLANT_NAMES = {
        "R": "Radishes",
        "C": "Clover",
        "G": "Grass",
        "V": "Violets"
    }

    DEFAULT_STUDENTS = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",        
        "Larry",
    ]

    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self._plants = [
            [self.PLANT_NAMES[encoding] for encoding in row]
            for row in diagram.split("\n")
        ]

        self._students = sorted(students)

    def plants(self, student) -> list[str]:
        i = self._students.index(student) * 2
        return self._plants[0][i:i+2] + self._plants[1][i:i+2]
