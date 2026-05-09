class Team:
    def __init__(self, name: str):
        self.name = name
        self.games_played = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def points(self):
        win_points = 3 * self.wins
        draw_points = 1 * self.draws
        return win_points + draw_points



def tally(rows):
    teams = []
    for game in rows:
        (team_name1, team_name2, result) = game.split(';')
        team1, team2 = None, None

        for index, team in enumerate(teams):
            if team_name1 == team.name:
                team1 = teams[index]
            if team_name2 == team.name:
                team2 = teams[index]

        if not team1:
            team1 = Team(name=team_name1)
            teams.append(team1)
        if not team2:
            team2 = Team(name=team_name2)
            teams.append(team2)

        team1.games_played += 1
        team2.games_played += 1

        if result == 'win':
            team1.wins += 1
            team2.losses +=1

        if result == 'loss':
            team1.losses += 1
            team2.wins += 1

        if result == 'draw':
            team1.draws += 1
            team2.draws += 1

    print(f'teams is {teams}')
    standings = []

    teams.sort(key=lambda team: (-team.points(), team.name))
    # teams.sort(key=lambda team: team.name)
    for team in teams:
        padded_team_name = team.name.ljust(30)
        padded_games_played = str(team.games_played).rjust(2)
        padded_points = str(team.points()).rjust(2)
        padded_wins = str(team.wins).rjust(2)
        padded_draws = str(team.draws).rjust(2)
        padded_losses = str(team.losses).rjust(2)

        standing = ' | '.join([padded_team_name, padded_games_played, padded_wins, padded_draws, padded_losses, padded_points])
        standings.append(standing)

    header = 'Team                           | MP |  W |  D |  L |  P'
    print(f'standings is {standings}')
    return [header] + standings


