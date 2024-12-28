import othello as othello
import ai_player as ai_player

othello = othello.Othello()

ai_player = ai_player.AIplayer('O')

print(ai_player.get_best_move(othello,5))