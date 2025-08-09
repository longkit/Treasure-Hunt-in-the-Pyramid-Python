# Project Report: Treasure Hunt in the Pyramid

## Overview  
This project implements a grid-based treasure hunt game combining Python and Prolog. The game features a player navigating a pyramid grid filled with traps to find a hidden treasure. It demonstrates a hybrid approach using Python for GUI and gameplay, and Prolog for logical pathfinding.

## Technologies  
- **Python 3** with **Pygame**: for rendering the game grid, traps, treasure, and player, plus handling the game loop.  
- **Prolog (SWI-Prolog)**: for running a Breadth-First Search (BFS) algorithm to find the shortest safe path from player to treasure avoiding traps.

## How it Works  
- The game grid is randomly populated with traps, a treasure, and the player’s starting position.  
- Prolog code computes the shortest valid path from player to treasure using BFS, considering trap locations as obstacles.  
- Python animates the player moving along this path step-by-step until the treasure is reached.  
- When the player reaches the treasure, the game resets with new random placements.

## Key Features  
- Random trap and treasure generation ensuring replayability.  
- Clear grid visualization using color-coded tiles for traps (red), treasure (blue), and player (green).  
- Automated player navigation based on Prolog’s pathfinding logic.  
- Modular design separating UI/gameplay and logical reasoning components.

## Challenges  
- Synchronizing Python’s graphical interface with Prolog’s logic engine for dynamic path updates.  
- Ensuring BFS correctly avoids traps and respects grid boundaries.  
- Maintaining smooth animation and game state updates during player movement.

## Future Enhancements  
- Full integration between Python and Prolog for real-time path recalculations as the game state changes.  
- Manual player control to complement automatic pathfinding.  
- Adding scoring, levels, and enhanced UI/UX elements like animations and sounds.  
- Expanding game complexity with new obstacle types and mechanics.

