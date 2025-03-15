# Graph-algos-visualization

Algorithm visualization on a 2D map with custom obstacles.

### Requirements
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-00A300?style=for-the-badge&logo=pygame&logoColor=white)

## Project Overview

This is a simple project designed to demonstrate the operation of various graph traversal algorithms in the context of a 2D grid. The main purpose is to visualize how these algorithms explore a grid, taking into account obstacles placed by the user. By using a 2D map as the graph, this project shows how different algorithms search for paths from a start point to an end point.

The project supports visualizing common graph algorithms, such as:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Dijkstra
- A* Search

## Features

- **Right-click to place start and end points**: The start point is green, and the end point is red.
- **Left-click to add obstacles**: Obstacles are marked in black on the grid.
- **Algorithm selection**: Choose the algorithm you want to visualize.
- **Reset functionality**: Clear the grid to start fresh and add new obstacles or change points.

## How to Use

1. **Set the Start and End Points:**
   - Right-click on the grid to place the **start point** (green).
   - Right-click again to place the **end point** (red).

2. **Add Obstacles:**
   - Left-click anywhere on the grid to add **black obstacles**.
   - Obstacles will block the path of the algorithms.

3. **Select an Algorithm:**
   - From the interface, select the graph traversal algorithm you wish to visualize (e.g., BFS, DFS, A*).

4. **Watch the Algorithm in Action:**
   - After selecting the algorithm, click the "Start" button to visualize how the algorithm explores the grid, finds paths, and avoids obstacles.

5. **Reset:**
   - Click the "Reset" button to clear the grid and start over. This will remove all obstacles and points.

## How It Works

The grid is a 2D array, with each cell representing a node in the graph. The start and end points are fixed nodes, and obstacles represent blocked nodes. The algorithms traverse this grid, searching for the shortest path between the start and end points while avoiding obstacles.

Each algorithm is visualized step by step, with nodes being highlighted as they are visited or processed. This allows you to observe how different algorithms behave under the same conditions.

- Inspired by classic pathfinding algorithms.

## To-Do List
💡Implement Dijkstra, A*
💡Think about graph representation
💡Improve the front-end to make it more pleasant

