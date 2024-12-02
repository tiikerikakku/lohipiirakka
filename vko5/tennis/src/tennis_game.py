class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, which):
        if which == self.player1_name:
            self.player1_score += 1
        else: # player 2
            self.player2_score += 1

    def _get_player_score_text(self, score):
        if score == 0:
            return 'Love'
        elif score == 1:
            return 'Fifteen'
        elif score == 2:
            return 'Thirty'
        elif score == 3:
            return 'Forty'

    def get_score(self):
        score = ''

        if self.player1_score == self.player2_score:
            if self.player1_score == 0: # both 0
                score = 'Love-All'
            elif self.player1_score == 1: # both 1
                score = 'Fifteen-All'
            elif self.player1_score == 2: # both 2
                score = 'Thirty-All'
            else: # both 4
                score = 'Deuce'
        elif self.player1_score >= 4 or self.player2_score >= 4:
            player1_player2_difference = self.player1_score - self.player2_score

            if player1_player2_difference == 1:
                score = 'Advantage player1'
            elif player1_player2_difference == -1:
                score = 'Advantage player2'
            elif player1_player2_difference >= 2:
                score = 'Win for player1'
            else:
                score = 'Win for player2'
        else: # scores under 4 and not same
            score = f'{self._get_player_score_text(self.player1_score)}' \
                    '-' \
                    f'{self._get_player_score_text(self.player2_score)}'

        return score
