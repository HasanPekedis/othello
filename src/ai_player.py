import random

class AIplayer:
    def __init__(self, player):
        self.depth = 0
        self.heuristic = "h1"
        self.player = player
        self.opponent = 'X' if player == 'O' else 'O'


    def decide_move(self, game):
        
        _, best_move = self.minimax(game, self.depth, True, self.heuristic)

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


    def minimax(self, game, depth, maximizing_player, heuristic):

        if depth == 0 or not game.has_valid_moves(self.player):
            if heuristic == 'h1':
                score = self.heuristic_h1(game)
            elif heuristic == 'h2':
                score = self.heuristic_h2(game)
            elif heuristic == 'h3':
                score = self.heuristic_h3(game)

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
                        eval_score, _ = self.minimax(game, depth - 1, False, heuristic)

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
                        eval_score, _ = self.minimax(game, depth - 1, True, heuristic)
                        # Undo the move
                        game.board = temp_board

                        if eval_score < min_eval:
                            min_eval = eval_score
                            best_move = (row, col)

            return min_eval, best_move

    def heuristic_h2(self, game):

        weight_matrix = [
            [100, 25, 10, 5, 5, 10, 25, 100],
            [25, 25, 2, 2, 2, 2, 25, 25],
            [10, 2, 5, 1, 1, 5, 2, 10],
            [5, 2, 1, 2, 2, 1, 2, 5],
            [5, 2, 1, 2, 2, 1, 2, 5],
            [10, 2, 5, 1, 1, 5, 2, 10],
            [25, 25, 2, 2, 2, 2, 25, 25],
            [100, 25, 10, 5, 5, 10, 25, 100],
        ]

        heuristic_value = 0

        # Calculate heuristic based on the weight matrix
        for row in range(len(game.board)):
            for col in range(len(game.board[row])):
                if game.board[row][col] == self.player:
                    heuristic_value += weight_matrix[row][col]
                elif game.board[row][col] == self.opponent:
                    heuristic_value -= weight_matrix[row][col]

        return heuristic_value
    
    def heuristic_h3(self, game):
    
        ai_valid_moves = len(game.get_valid_moves(self.player))
        opponent_valid_moves = len(game.get_valid_moves(self.opponent))

        # Calculate heuristic value
        heuristic_value = ai_valid_moves - opponent_valid_moves
        return heuristic_value
    
    

