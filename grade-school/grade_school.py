import collections

class School:
    """Manages a school roster with students organized by grade level.
    
    This implementation uses a lazy sorting strategy optimized for read-heavy
    workloads, where roster queries are more frequent than student additions.
    
    Internal Data Structure:
        _roster: defaultdict[int, list[str]]
            Maps grade levels to lists of student names
            e.g., {1: ["Alice", "Bob"], 2: ["Charlie", "Diana"]}
            Uses defaultdict to automatically create empty lists for new grades
        
        _added: list[bool] 
            Tracks the success/failure of each add_student() operation
            Parallel to the sequence of add_student() calls
            
        _roster_dirty: bool
            Dirty flag for lazy sorting optimization
            Set to True when students are added, False after sorting
            Prevents unnecessary re-sorting of unchanged data
    """

    def __init__(self):
        self._roster = collections.defaultdict(list)
        self._added = []
        self._roster_dirty = False

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
            self._roster[grade].append(name)
            self._added.append(True)
            self._roster_dirty = True

    def roster(self) -> list[str]:
        """Get all student names in the school.
        
        Returns:
            A list of all student names, sorted by grade level first,
            then alphabetically by name within each grade.
        """
        self._lazy_sort_roster()

        student_names = []
        grades = sorted(self._roster.keys())

        for grade in grades:
            student_names.extend(self._roster[grade])

        return student_names


    def grade(self, grade: int) -> list[str]:
        """Get all student names in a specific grade.
        
        Args:
            grade: The grade level to filter by
            
        Returns:
            A list of student names in the specified grade,
            sorted alphabetically by name.
        """
        self._lazy_sort_roster()
        return self._roster[grade]

    def added(self) -> list[bool]:
        return self._added

    def _roster_contains(self, name) -> bool:
        for _grade, names in self._roster.items():
            if any(student_name == name for student_name in names):
                return True
        return False


    def _lazy_sort_roster(self) -> None:
        if not self._roster_dirty:
            return

        for grade in self._roster.keys():
            self._roster[grade].sort()

        self._roster_dirty = False
