# 🗺️A-Maze-ing
### 📌 Description:
#### A maze project is a program that generates and solves a grid-based maze. It reads configuration settings and creates a structured path between an entry and an exit point. The goal is to find a valid route through the maze and display the solution clearly.

### 🧩 Features:
####  Reads and validates `config.txt`
- Checks for missing or duplicate keys
- Creates a maze using width and height
- Handles entry and exit coordinates
- Supports perfect or imperfect maze generation
- Displays the maze in the terminal
- Saves the result to an output file
- Provides clear error messages

### 🧠 Algorithms used for solving the maze:
#### 🔄 Depth-First-Search (DFS): 
 DFS is used to explore the maze by going as deep as possible along one path before backtracking.
It is commonly used for maze generation and solving.
#### ↔️ Breadth-First-Search (BFS):
BFS explores the maze level by level.
It guarantees the shortest path between entry and exit.
#### 🖥️ Curses library:
The curses library is used to create a terminal-based graphical interface.
It allows drawing the maze and updating the screen dynamically.
#### ➡️ Binary Tree:
A maze generation technique that removes walls between cells, usually choosing randomly between two directions (commonly right or down), to create a perfect maze with one unique path between any two points.

### 📂 Project Structure:
- `Makefile` : The Makefile is used to simplify running and managing the project.

- `config.txt` : The config.txt file contains the configuration settings required to run the maze program.  
- **WIDTH** – The width of the maze.
- **HEIGHT** – The height of the maze.
- **ENTRY** – The starting coordinates.
- **EXIT** – The ending coordinates.
- **OUTPUT_FILE** – The output file name.
- **PERFECT** – Maze type (TRUE or FALSE).

- `src/algos.py`: This file contains the main algorithms used in the project, including maze generation and solving techniques such as DFS, BFS, and Binary Tree. It handles the logic of finding paths and processing the maze structure.

- `src/grid.py`: This file contains the main maze structure and display logic. It is responsible for creating the grid, generating special blocks, printing the maze in the terminal, converting cells to hexadecimal format, and writing the final output to a file.
- `src/read_config.py`: This function reads and parses the config.txt file. It validates all required keys and their values, checks for errors such as missing, duplicate, or invalid data, and raises a config_exception when an error is detected. It returns a dictionary containing the validated configuration settings.
- `main`: This is the main entry point of the project. It loads the configuration, initializes the maze, calls the generation and solving algorithms, handles user interaction (if using curses), and coordinates all components of the program.