from collections import defaultdict

class Team:
    def __init__(self):
        self.name = None
        self.matches_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0

    def points(self) -> int:
        win_points = 3 * self.wins
        draw_points = 1 * self.draws
        return win_points + draw_points


def tally(rows):
    teams = _tabulate_team_records(rows)
    sorted_teams = sorted(teams.values(), key=lambda team: (-team.points(), team.name))

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
            str(team.points()).rjust(2),
        ])
        all_teams_stats.append(team_stats)
    return all_teams_stats


def _tabulate_team_records(rows) -> list[Team]:
    teams = defaultdict(Team)
    for row in rows:
        team_name1, team_name2, result = row.split(';')

        team1 = teams[team_name1]
        team2 = teams[team_name2]
        if team1.name is None:
            team1.name = team_name1
        if team2.name is None:
            team2.name = team_name2

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
            team2.draws +=1
