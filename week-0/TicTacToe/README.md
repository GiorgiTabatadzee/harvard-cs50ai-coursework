Tic-Tac-Toe AI

This project implements an AI that plays Tic-Tac-Toe optimally using the Minimax algorithm in Python 3.12. The AI is unbeatable when both players play optimally.

Overview

The game is represented as a 3x3 board. Players take turns placing their marks (X or O) until one wins or the board is full.

This project focuses on implementing the game logic and AI in tictactoe.py, while runner.py handles the graphical interface.

Features

Optimal AI: Uses Minimax to choose the best possible move.

Game State Management: Functions to check available moves, apply moves, and determine winners.

Terminal and Utility Functions: Determines when the game ends and assigns utility values for AI decisions.

Getting Started

Download the project distribution from:
Tic-Tac-Toe Project

Unzip the files into your project directory.

Install required packages:

pip3 install -r requirements.txt


Run the game:

python runner.py

File Structure

tictactoe.py – Contains the game logic and AI implementation. You will implement the following functions:

player(board) – Returns which player's turn it is (X or O).

actions(board) – Returns all possible moves on the current board.

result(board, action) – Returns the new board state after a move.

winner(board) – Returns the winner (X or O) if there is one, otherwise None.

terminal(board) – Returns True if the game is over, else False.

utility(board) – Returns the utility value: 1 if X wins, -1 if O wins, 0 for a tie.

minimax(board) – Returns the optimal move for the current player.

runner.py – Pre-built graphical interface to play the game against the AI.

Gameplay Rules

The first move is always X.

Players alternate turns.

The game ends when a player wins (three in a row horizontally, vertically, or diagonally) or when all cells are filled (tie).

AI Details

The AI uses the Minimax algorithm to evaluate all possible moves and chooses the optimal one. If multiple moves are equally good, any of them may be selected.

Notes

The AI cannot be beaten if it plays optimally.

All functions assume valid input boards (3x3 with X, O, or EMPTY).

The original board is never modified by the AI, allowing Minimax to explore multiple future states.