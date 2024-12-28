import othello as othello
import ai_player as ai_player

othello = othello.Othello()

ai_player = ai_player.AIplayer('O')

print(ai_player.decide_move(othello, 3, 'h2')) 