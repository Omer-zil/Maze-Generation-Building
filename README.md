# Maze Generator and Solver

This project generates and solves a random maze using Python and Tkinter.

## Features

- Random maze generation
- DFS (Depth First Search) using a stack
- Dynamic wall removal animation
- Maze solving using backtracking
- Red dots show current mouse movement
- Blue dots show dead ends
- Green dots show the correct path
- Bonus feature: random extra wall removal creates cycles

## Maze Representation

The maze uses two arrays:

- northWall[row][col]
- eastWall[row][col]

A value of 1 means the wall exists.
A value of 0 means the wall has been removed.

## Maze Generation

The maze is generated using a stack-based DFS algorithm.

The “mouse”:
1. Starts at a random cell
2. Chooses a random unvisited neighbor
3. Removes the wall
4. Moves to the next cell
5. Backtracks when trapped

## Data Structure
1. 2D arrays for walls:
 1.1 northWall
 1.2 eastWall
2. Visited arrays:
 2.1visited
 2.2solverVisited
3. Stack for DFS implementation

## Maze Solving

The maze is solved using recursive backtracking.

- Red = current position
- Blue = dead end
- Green = final solution path

## Bonus Challenge

A random extra wall is removed with a 1 in 20 chance to create cycles in the maze.

## How to Run

python maze_GUI.py

## Done By

Omer Abubeker  /
ID UGR/6702/16  /
Section 2