# Treasure Hunt in the Pyramid

This project is a grid-based treasure hunt game implemented using Python and Prolog.

## Overview

- The **Python** part uses Pygame to create a graphical interface where a player navigates a pyramid grid, avoiding traps and searching for a hidden treasure.
- The grid consists of traps (red), the treasure (blue), and the player (green).
- The player automatically moves step-by-step towards the treasure using the shortest path computed by the **Prolog** program.
- The **Prolog** code performs a Breadth-First Search (BFS) to find the valid shortest path on the grid, avoiding traps.

## Features

- Random placement of player, treasure, and traps on a grid.
- Visual grid display with color-coded cells.
- Automated player movement using BFS pathfinding implemented in Prolog.
- Resetting the game upon treasure discovery.

## Requirements

- Python 3.x
- Pygame library (`pip install pygame`)
- SWI-Prolog (or compatible Prolog interpreter) for running pathfinding logic.

## How to Run

1. Run the Python script `game.py` to launch the GUI and start the game.
2. Prolog code is used for pathfinding; integration can be done via inter-process communication or embedding Prolog queries in Python (not included in this demo).
3. The player will move stepwise towards the treasure while avoiding traps.

## Future Improvements

- Integrate Prolog and Python for dynamic pathfinding.
- Add manual player controls.
- Include more complex traps and game mechanics.
- Save game states and scores.


