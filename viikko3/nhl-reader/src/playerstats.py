class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        
    def point(self, p):
        return p.points
        
    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players(nationality)
        players.sort(key=self.point, reverse=True)
        return players
        
