import time
import random
from ai_player import AIplayer
from othello import Othello

class RandomPlayer:
    def __init__(self, player):
        self.player = player

    def decide_move(self, game):
        valid_moves = game.get_valid_moves(self.player)
        return random.choice(valid_moves) if valid_moves else None

class Benchmark:
    def __init__(self, num_games=10):
        self.num_games = num_games

    def run_benchmark(self):
        results = []
        heuristics = ['h1', 'h2', 'h3']
        depths = [1, 2, 3]

        for heuristic in heuristics:
            for depth in depths:
                print(f"Testing AI with {heuristic} at depth {depth} vs Random Player")
                result = self.test_ai_vs_random(heuristic, depth)
                results.append(result)

        self.display_results(results)

    def test_ai_vs_random(self, heuristic, depth):
        ai_wins = 0
        random_wins = 0
        draws = 0
        total_time = 0

        for game_number in range(self.num_games):
            print(f"Starting game {game_number + 1}...")
            game = Othello()
            ai_player = AIplayer('X')
            ai_player.depth = depth
            ai_player.heuristic = heuristic
            random_player = RandomPlayer('O')

            start_time = time.time()
            winner = game.play_ai_vs_random(ai_player, random_player)  # Assume this method exists
            end_time = time.time()

            total_time += (end_time - start_time)

            if winner == 'X':
                ai_wins += 1
            elif winner == 'O':
                random_wins += 1
            else:
                draws += 1

        avg_time = total_time / self.num_games
        accuracy = (ai_wins / self.num_games) * 100  # Calculate accuracy as a percentage
        print(f"AI Wins: {ai_wins}, Random Wins: {random_wins}, Draws: {draws}, Avg Time: {avg_time:.2f} seconds, Accuracy: {accuracy:.2f}%")

        return {
            'heuristic': heuristic,
            'depth': depth,
            'ai_wins': ai_wins,
            'random_wins': random_wins,
            'draws': draws,
            'avg_time': avg_time,
            'accuracy': accuracy
        }

    def display_results(self, results):
        print("\nBenchmark Results:")
        for result in results:
            print(f"Heuristic: {result['heuristic']}, Depth: {result['depth']}, AI Wins: {result['ai_wins']}, Random Wins: {result['random_wins']}, Draws: {result['draws']}, Avg Time: {result['avg_time']:.2f} seconds, Accuracy: {result['accuracy']:.2f}%")

if __name__ == "__main__":
    benchmark = Benchmark(num_games=5)  # Adjust the number of games as needed
    benchmark.run_benchmark()
