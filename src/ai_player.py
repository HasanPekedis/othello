import random

class AI_player:
    def __init__(self, player, depth):
        self.player = player
        self.opponent = 'X' if player == 'O' else 'O'
        self.depth = depth

    def decide_move(self, othello):
        best_move = None
        valid_moves = othello.get_valid_moves(self.player)
        if valid_moves:
            best_move = random.choice(valid_moves)
        return best_move


