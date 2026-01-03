class HighScores:
    """Manages a list of game scores and provides access to score statistics."""

    def __init__(self, scores) -> None:
        """Initialize with a list of scores."""
        self._scores = scores

    @property
    def scores(self) -> list[int]:
        """Return all scores."""
        return self._scores

    def latest(self) -> int:
        """Return the most recent score."""
        return self._scores[-1]

    def personal_best(self) -> int:
        """Return the highest score achieved."""
        return max(self._scores)

    def personal_top_three(self) -> list[int]:
        """Return the top three scores in descending order."""
        return sorted(self._scores, reverse=True)[:3]
