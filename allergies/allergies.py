class Allergies:
    ALLERGENS = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats",
    ]

    def __init__(self, score: int) -> None:
        """Initialize allergy test results from binary-encoded score."""
        self._test_results = {}
        remaining = score # avoid mutating passed-in parameters
        for allergen in self.ALLERGENS:
            # Check if the current bit is set, then shift to the next bit
            self._test_results[allergen] = remaining % 2 == 1
            remaining = remaining // 2

    def allergic_to(self, item: str) -> bool:
        """Return whether person is allergic to the given item."""
        return self._test_results[item]

    @property
    def lst(self) -> list[str]:
        """Return list of allergens that tested positive."""
        return [
            allergen
            for allergen, positive in self._test_results.items()
            if positive
        ]
