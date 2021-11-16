class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = self.assists + self.goals

    def __str__(self):
        return f"{self.name:25} {self.team} {str(self.goals):>2} + {str(self.assists):>2} = {str(self.points):2} "
