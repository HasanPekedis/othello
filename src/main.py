import othello as othello
from ai_player import AIplayer  # Assuming AIPlayer is in a separate module

def configure_ai_player(player_type):
    """
    Configures an AI player with depth and heuristic type.
    :param player_type: String indicating the player type ('AI 1' or 'AI 2').
    :return: A dictionary with AI configuration.
    """
    print(f"Configuring {player_type}...")
    depth = int(input(f"Enter search depth for {player_type} (e.g., 3): ").strip())
    print("Select heuristic type:")
    print("1. h1 - Disc Difference")
    print("2. h2 - Positional Advantage")
    print("3. h3 - Mobility")
    heuristic_choice = input(f"Choose heuristic for {player_type} (1, 2, or 3): ").strip()

    if heuristic_choice == '1':
        heuristic = 'h1'
    elif heuristic_choice == '2':
        heuristic = 'h2'
    elif heuristic_choice == '3':
        heuristic = 'h3'
    else:
        print("Invalid choice. Defaulting to h1.")
        heuristic = 'h1'

    return {'depth': depth, 'heuristic': heuristic}

print("Welcome to Othello!")
print("1. Human Player vs Human Player")
print("2. Human Player vs AI Player")
print("3. AI Player vs AI Player")
choice = input("Select a game mode (1, 2, or 3): ").strip()

othello = othello.Othello()

if choice == '1':
    othello.play_human_vs_human()
elif choice == '2':
    # Configure AI player
    ai_config = configure_ai_player("AI Player")
    ai_player = AIplayer('O')  # Assuming AI player is 'X'
    ai_player.depth = ai_config['depth']
    ai_player.heuristic = ai_config['heuristic']
    othello.play_human_vs_ai(ai_player)
elif choice == '3':
    # Configure both AI players
    ai1_config = configure_ai_player("AI 1")
    ai2_config = configure_ai_player("AI 2")
    ai_player_1 = AIplayer('X')  # AI 1 is 'X'
    ai_player_2 = AIplayer('O')  # AI 2 is 'O'
    ai_player_1.depth = ai1_config['depth']
    ai_player_1.heuristic = ai1_config['heuristic']
    ai_player_2.depth = ai2_config['depth']
    ai_player_2.heuristic = ai2_config['heuristic']
    othello.play_ai_vs_ai(ai_player_1, ai_player_2)
else:
    print("Invalid choice. Exiting.")