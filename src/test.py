import othello as othello
import ai_player as ai_player

othello = othello.Othello()

ai_player = ai_player.AIplayer('X')
ai_player.depth = 3
ai_player.heuristic = 'h1'


print(othello.has_valid_moves('O')) # Expected output: True