import othello as othello


print("Welcome to Othello!")
print("1. Human Player vs Human Player")
print("2. Human Player vs AI Player")
print("3. AI Player vs AI Player")
choice = input("Select a game mode (1, 2, or 3): ").strip()

othello = othello.Othello()

if choice == '1':
    othello.play_human_vs_human()
elif choice == '2':
    othello.play_human_vs_ai()
elif choice == '3':
    othello.play_ai_vs_ai()
else:
    print("Invalid choice. Exiting.")


