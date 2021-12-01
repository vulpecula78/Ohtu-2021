class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def score_to_str(self, player1_score, player2_score):
        score_names = {0: "Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}
        if player1_score == player2_score:
            if player1_score > 3:
                return "Deuce"
            else:
                return score_names[player1_score] + "-" + "All"
        else:
            return score_names[player1_score] + "-" + score_names[player2_score]

    def get_result(self, difference):
        if difference == 1:
            return f"Advantage {self.player1_name}"
        elif difference == -1:
            return f"Advantage {self.player2_name}"
        elif difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def get_score(self): 
        if self.p1_score == self.p2_score:
            score = self.score_to_str(self.p1_score, self.p2_score)
        elif self.p1_score >= 4 or self.p2_score >= 4:
            score = self.get_result(self.p1_score - self.p2_score)            
        else:
            score = self.score_to_str(self.p1_score, self.p2_score)
        return score
