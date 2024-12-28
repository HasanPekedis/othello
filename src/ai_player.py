import random

class AIplayer:
    def __init__(self, player):
        self.player = player
        self.opponent = 'X' if player == 'O' else 'O'


    def decide_move(self, game, depth):

        _, best_move = self.minimax(game, depth, True)
        if best_move:
            row, col = best_move
            return f"{row + 1}{chr(col + ord('a'))}"
        return None
    
    def heuristic_h1(self, game):
        player_count = 0
        opponent_count = 0

        for row in game.board:
            for cell in row:
                if cell == self.player:
                    player_count += 1
                elif cell == self.opponent:
                    opponent_count += 1

        return player_count - opponent_count

    def minimax(self, game, depth, maximizing_player):

        if depth == 0 or not game.has_valid_moves(self.player):
            score = self.heuristic_h1(game)
            return score, None

        best_move = None

        if maximizing_player:
            max_eval = float('-inf')
            for row in range(game.board_size):
                for col in range(game.board_size):
                    if game.is_valid_move(row, col, self.player):
                        # Simulate the move
                        temp_board = [r[:] for r in game.board]
                        game.apply_move(row, col, self.player)

                        # Recursive call
                        eval_score, _ = self.minimax(game, depth - 1, False)
                        print(eval_score)

                        # Undo the move
                        game.board = temp_board

                        if eval_score > max_eval:
                            max_eval = eval_score
                            best_move = (row, col)

            return max_eval, best_move

        else:
            min_eval = float('inf')
            for row in range(game.board_size):
                for col in range(game.board_size):
                    if game.is_valid_move(row, col, self.opponent):
                        # Simulate the move
                        temp_board = [r[:] for r in game.board]
                        game.apply_move(row, col, self.opponent)

                        # Recursive call
                        eval_score, _ = self.minimax(game, depth - 1, True)
                        print(eval_score)
                        # Undo the move
                        game.board = temp_board

                        if eval_score < min_eval:
                            min_eval = eval_score
                            best_move = (row, col)

            return min_eval, best_move
        
    

