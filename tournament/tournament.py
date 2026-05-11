from dataclasses import dataclass

@dataclass
class Team:
    name: str
    matches_played: int = 0
    wins: int = 0
    draws: int = 0
    losses: int = 0

    @property
    def points(self) -> int:
        return 3 * self.wins + self.draws


def tally(rows: list[str]) -> list[str]:
    teams = _tabulate_team_records(rows)
    sorted_teams = sorted(teams.values(), key=lambda team: (-team.points, team.name))

    heading = f'{'Team':<30} | MP |  W |  D |  L |  P'
    team_stats = _format_team_stats(sorted_teams)
    return [heading] + team_stats

def _format_team_stats(teams: list[Team]) -> list[str]:
    return [
        f'{team.name:<30} | {team.matches_played:>2} | {team.wins:>2} | '
        f'{team.draws:>2} | {team.losses:>2} | {team.points:>2}'
        for team in teams
    ]


def _tabulate_team_records(rows: list[str]) -> dict[str, Team]:
    teams = {}
    for row in rows:
        team_name1, team_name2, result = row.split(';')
        team1 = teams.setdefault(team_name1, Team(team_name1))
        team2 = teams.setdefault(team_name2, Team(team_name2))

        _update_records_from_result(team1, team2, result)
    return teams

def _update_records_from_result(team1: Team, team2: Team, result: str) -> None:
    team1.matches_played += 1
    team2.matches_played += 1

    match result:
        case 'win':
            team1.wins += 1
            team2.losses += 1
        case 'loss':
            team1.losses += 1
            team2.wins += 1
        case 'draw':
            team1.draws += 1
            team2.draws += 1
