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


def tally(rows):
    teams = _tabulate_team_records(rows)
    sorted_teams = sorted(teams.values(), key=lambda team: (-team.points, team.name))

    heading = "Team                           | MP |  W |  D |  L |  P"
    team_stats = _format_team_stats(sorted_teams)
    return [heading] + team_stats

def _format_team_stats(teams) -> list[str]:
    all_teams_stats = []
    for team in teams:
        team_stats = ' | '.join([
            team.name.ljust(30),
            str(team.matches_played).rjust(2),
            str(team.wins).rjust(2),
            str(team.draws).rjust(2),
            str(team.losses).rjust(2),
            str(team.points).rjust(2),
        ])
        all_teams_stats.append(team_stats)
    return all_teams_stats


def _tabulate_team_records(rows) -> dict[str, Team]:
    teams = {}
    for row in rows:
        team_name1, team_name2, result = row.split(';')
        team1 = teams.setdefault(team_name1, Team(team_name1))
        team2 = teams.setdefault(team_name2, Team(team_name2))

        _update_records_from_result(team1, team2, result)
    return teams

def _update_records_from_result(team1, team2, result):
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
