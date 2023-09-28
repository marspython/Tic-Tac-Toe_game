# Tic-Tac-Toe Game project with Tkinter GUI

This Python project implements a simple Tic-Tac-Toe game with a graphical user interface (GUI) using the Tkinter library. Players can take turns to make moves, and the game checks for a win, draw, or continuation. The game allows players to start a new round or exit the application after each game.

## How to Play

- **Objective**: The goal of the game is to be the first to form a line of three of your symbols ('X' or 'O') either horizontally, vertically, or diagonally on the game board.

- **Player**: You will play as 'X'. The computer or another player can take the 'O' role.

- **Game Rules**: 
  - Players take turns to make a move by clicking on an empty cell of the game board.
  - 'X' always goes first.
  - Once a cell is selected, it will be marked with 'X' (your symbol).
  - The game checks for a win after each move and declares the winner if a line of 'X' or 'O' is formed.
  - If no player forms a line, and all cells are filled, the game ends in a draw.
  - After each game, you have the option to play again or exit the application.

## How to Run

1. **Prerequisites**: Ensure you have Python 3.x installed on your system.

2. **Run the Game**:
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Run the following command to start the game:
     ```
     python tic_tac_toe.py
     ```

## Project Structure

- `tic_tac_toe.py`:
  - Imports the necessary modules (Tkinter and `messagebox`).
  - Defines a `display_message` function to show informational messages using `messagebox.showinfo`.
  - Creates the main `TicTacToeGUI` class to manage the game.
  - Initializes the Tkinter window and sets up the game board buttons.
  - Implements methods to make moves, check for a win or draw, and display game outcomes.
  - Handles player decisions to play again or exit the game.
  - Runs the main game loop using `self.window.mainloop()`.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE.md).
