# Othello Game Project

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation Instructions](#installation-instructions)
5. [Usage](#usage)
6. [Code Structure](#code-structure)
7. [Contributing](#contributing)
8. [License](#license)

## Description
The Othello Game Project is a Python-based implementation of the classic board game Othello (also known as Reversi). The project allows users to play the game in various modes, including Human vs Human, Human vs AI, and AI vs AI. The AI players utilize different heuristics and search depths to make strategic moves, providing a challenging experience for human players.

## Features
- **Multiple Game Modes**: Play against another human, against an AI, or watch two AI players compete.
- **Customizable AI**: Configure the AI's search depth and heuristic strategy to adjust difficulty.
- **Heuristic Strategies**: The AI uses three different heuristics:
  - **h1**: Disc Difference - Focuses on maximizing the difference in the number of discs.
  - **h2**: Positional Advantage - Prioritizes controlling strategic positions on the board.
  - **h3**: Mobility - Aims to maximize the number of valid moves available.
- **Benchmarking**: A benchmarking module is included to test the performance of different AI configurations against a random player.
- **Interactive Gameplay**: The game provides an interactive command-line interface for players to input their moves.

## Technologies Used
- **Python**: The core programming language used for the project.
- **Minimax Algorithm**: Used by the AI to make decisions based on the current state of the board.
- **Heuristic Evaluation**: Different heuristics are implemented to guide the AI's decision-making process.
- **Command-Line Interface (CLI)**: The game is played and interacted with via the terminal.

## Installation Instructions
To set up and run the Othello Game Project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/othello.git
   cd othello
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.x installed. No additional dependencies are required.

3. **Run the Game**:
   Navigate to the `src` directory and run the `main.py` file:
   ```bash
   cd src
   python main.py
   ```

4. **Follow On-Screen Instructions**:
   The game will prompt you to select a game mode and configure AI settings if applicable.

## Usage
### Starting the Game
After running `main.py`, you will be presented with the following options:
1. **Human Player vs Human Player**: Two human players can take turns to play the game.
2. **Human Player vs AI Player**: Play against an AI with configurable depth and heuristic.
3. **AI Player vs AI Player**: Watch two AI players compete against each other.

### Configuring the AI
When playing against or with AI players, you will be prompted to configure:
- **Search Depth**: Determines how many moves ahead the AI will look.
- **Heuristic**: Choose between `h1`, `h2`, or `h3` to define the AI's strategy.

### Example Gameplay
1. **Human vs AI**:
   - Select option `2` when prompted.
   - Configure the AI's depth and heuristic.
   - Enter your moves in the format `3d` (row `3`, column `d`).

2. **AI vs AI**:
   - Select option `3` when prompted.
   - Configure both AI players.
   - Watch the AI players compete and see the final result.

### Benchmarking
To run the benchmark and test AI performance:
1. Navigate to the `src` directory.
2. Run the `benchmark.py` file:
   ```bash
   python benchmark.py
   ```
3. The benchmark will test different AI configurations against a random player and display the results.

## Code Structure
The project is organized as follows:
- **`main.py`**: The entry point of the application, handling game mode selection and AI configuration.
- **`othello.py`**: Contains the core game logic, including board management, move validation, and game flow.
- **`ai_player.py`**: Implements the AI player using the Minimax algorithm with heuristic evaluation.
- **`benchmark.py`**: A module for benchmarking AI performance against a random player.
- **`test.py`**: Contains test cases for validating game logic.

## Contributing
Contributions to the Othello Game Project are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

