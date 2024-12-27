import ai_player as ai_player
class Othello:
    def __init__(self):
        self.board_size = 8
        self.board = [['.' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.initialize_board()

    def initialize_board(self):
        # Place the initial 4 pieces in the center
        mid = self.board_size // 2
        self.board[mid - 1][mid - 1] = 'O'
        self.board[mid][mid] = 'O'
        self.board[mid - 1][mid] = 'X'
        self.board[mid][mid - 1] = 'X'

    def print_board(self):
        column_labels = "  a b c d e f g h"
        print(column_labels)
        for i, row in enumerate(self.board):
            print(f"{i + 1} " + " ".join(row))
        print(column_labels)

    def is_valid_move(self, row, col, player):
        if self.board[row][col] != '.':
            return False

        opponent = 'X' if player == 'O' else 'O'
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            has_opponent_between = False

            while 0 <= r < self.board_size and 0 <= c < self.board_size:
                if self.board[r][c] == opponent:
                    has_opponent_between = True
                elif self.board[r][c] == player and has_opponent_between:
                    return True
                else:
                    break

                r += dr
                c += dc

        return False

    def get_valid_moves(self, player):
        valid_moves = []

        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.is_valid_move(row, col, player):
                    valid_moves.append((row, col))
        
        # Convert valid moves to the desired format
        formatted_moves = [f"{row + 1}{chr(col + ord('a'))}" for row, col in valid_moves]
        print(formatted_moves)
        return formatted_moves

    def apply_move(self, row, col, player):
        opponent = 'X' if player == 'O' else 'O'
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        self.board[row][col] = player

        for dr, dc in directions:
            r, c = row + dr, col + dc
            pieces_to_flip = []

            while 0 <= r < self.board_size and 0 <= c < self.board_size:
                if self.board[r][c] == opponent:
                    pieces_to_flip.append((r, c))
                elif self.board[r][c] == player:
                    for pr, pc in pieces_to_flip:
                        self.board[pr][pc] = player
                    break
                else:
                    break

                r += dr
                c += dc

    def has_valid_moves(self, player):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.is_valid_move(row, col, player):
                    return True
        return False

    def print_game_result(self):
        self.print_board()
        x_count = sum(row.count('X') for row in self.board)
        o_count = sum(row.count('O') for row in self.board)
        print(f"Game over. X: {x_count}, O: {o_count}")
        if x_count > o_count:
            print("X wins!")
        elif o_count > x_count:
            print("O wins!")
        else:
            print("It's a tie!")
    
    def play_human_vs_human(self):
        current_player = 'X'

        while True:
            print(30 * "=")
            self.print_board()
            if not self.has_valid_moves(current_player):
                print(f"{current_player} has no valid moves. Skipping turn.")
                current_player = 'X' if current_player == 'O' else 'O'
                if not self.has_valid_moves(current_player):
                    print("No players have valid moves. Game over.")
                    break
                continue

            print(f"{current_player}'s turn.")
            try:
                move = input("Enter move (e.g., 3d): ").strip()
                if len(move) == 2 and move[0].isdigit() and move[1].isalpha():
                    row = int(move[0]) - 1
                    col = ord(move[1].lower()) - ord('a')
                    if 0 <= row < self.board_size and 0 <= col < self.board_size and self.is_valid_move(row, col, current_player):
                        self.apply_move(row, col, current_player)
                        current_player = 'X' if current_player == 'O' else 'O'
                    else:
                        print("Invalid move. Try again.")
                else:
                    print("Invalid input. Please enter row and column in the format (e.g., 3d).")
            except ValueError:
                print("Invalid input. Please enter row and column in the format (e.g., 3d).")

        self.print_game_result()


    def play_human_vs_ai(self):
        current_player = 'X'
        ai_player_digit = 'O'

        ai = ai_player.AI_player(ai_player_digit, 0)

        while True:
            print(30 * "=")
            self.print_board()
            if not self.has_valid_moves(current_player):
                print(f"{current_player} has no valid moves. Skipping turn.")
                current_player = 'X' if current_player == 'O' else 'O'
                if not self.has_valid_moves(current_player):
                    print("No players have valid moves. Game over.")
                    break
                continue

            print(f"{current_player}'s turn.")
            try:
                if current_player == ai_player_digit:
                    print("AI can play: ")
                    move = ai.decide_move(self)
                    print(f"AI player moves to " + move)
                else:
                    print("You can play: ")
                    self.get_valid_moves(current_player)
                    move = input("Enter move (e.g., 3d): ").strip()

                if len(move) == 2 and move[0].isdigit() and move[1].isalpha():
                    row = int(move[0]) - 1
                    col = ord(move[1].lower()) - ord('a')
                    if 0 <= row < self.board_size and 0 <= col < self.board_size and self.is_valid_move(row, col, current_player):
                        self.apply_move(row, col, current_player)
                        current_player = 'X' if current_player == 'O' else 'O'
                    else:
                        print("Invalid move. Try again.")
                else:
                    print("Invalid input. Please enter row and column in the format (e.g., 3d).")
            except ValueError:
                print("Invalid input. Please enter row and column in the format (e.g., 3d).")

        self.print_game_result()

