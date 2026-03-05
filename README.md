*This project has been created as part of the 42 curriculum by sasarbou, khnoman.*
# 🗺️A-Maze-ing
### 📌 Description:
#### A maze project is a program that generates and solves a grid-based maze. It reads configuration settings and creates a structured path between an entry and an exit point. The goal is to find a valid route through the maze and display the solution clearly.

### The chosen maze algorithms:
 - Maze Generation:   DFS Backtracking Algorithm,
DFS was chosen because it is simple to implement, generates perfect mazes efficiently, and allows easy addition of non-perfect variations.  
- Maze solving:  Breadth-First Search (BFS) for shortest path.

### 🧩 Features:
####  Reads and validates `config.txt`
- Checks for missing or duplicate keys
- Creates a maze using width and height
- Handles entry and exit coordinates
- Supports perfect or imperfect maze generation
- Displays the maze in the terminal
- Saves the result to an output file
- Provides clear error messages

### Instructions:
#### Requirements:
- Python 3.x
- curses library (available by default on Unix systems)
- A valid config.txt file in the root directory
#### Installation
- No compilation is required.
- Make sure Python 3 is installed on your system.
- you can also use Makefile `make run` to run your project without using command lines every time you want to excute your project
#### Execution
- Run your program with :   `python3 a-maze-ing.py`, or with `make run`

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

### Resources

Here are the external resources we used to understand and implement the algorithms and concepts in this project:

- **Depth-First Search (DFS) Documentation**  
  Used to understand the maze generation algorithm and backtracking technique.  
  https://www.geeksforgeeks.org/dsa/depth-first-search-or-dfs-for-a-graph/

- **Breadth-First Search (BFS) Documentation**  
  Used to implement the shortest path algorithm for solving the maze.  
  https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

- **Python Curses Documentation**  
  Used to create the terminal-based interface and visualize the maze dynamically.  
  https://docs.python.org/3/howto/curses.html

### 👥 The Team and Poject Management:
#### Khawla's Roles:   
- DFS algorithm for  Creates Perfect Mazes.
- grid generator with 42 obstacle.
- make maze NON-PERFECT (Add Extra Openings).
- Generation of the output file for an Hexadecimal representation of the maze.
- Animation & Visualization.
- User Interface Handling.
- Main program integration and coordination.
- Testing & Debugging.
- Performance Optimization.
#### Sara's Roles:
- BFS alorithm for finding the shortest path between Entry and Exit.
- parsing of `config.txt` file.
- `Makefile` file.
- Code organization into reusable modules(packaging).
- `README.md` file.
- Testing & Debugging.
- Performance Optimization.
- Main program integration and coordination.

#### Tools:
Examples of Tools:

- 🐍 Python – programming language used to write the project

- 🧭 curses – library used for terminal interface and visualization

- 🗂 Git – version control system

- 💻 VS Code – code editor

- 🛠 Makefile – used to simplify running the project