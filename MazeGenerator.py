from mazegen.grid import create_maze, create_block_42, print_maze, write_hex_output
from mazegen.algos import dfs, non_perfect, find_shortest_path_bfs

class MazeGenerator:
    def __init__(self, config):
        self.width = config["WIDTH"]
        self.height = config["HEIGHT"]
        self.entry = tuple(config["ENTRY"])
        self.exit_end = tuple(config["EXIT"])
        self.out_file = config["OUTPUT_FILE"]
        self.perfect = config["PERFECT"] in ["TRUE", 1]

        self.maze = None
        self.block_42 = None
        self.path = []
        self.moves = 0

    def generate_maze(self):
        """Create a new maze and compute path."""
        self.maze = create_maze(self.width, self.height)
        self.block_42 = create_block_42(self.width, self.height, self.entry, self.exit_end)

        dfs(self.maze, self.width, self.height, start=self.entry, block_42=self.block_42)

        if not self.perfect:
            non_perfect(self.maze, self.width, self.height, self.block_42)

        self.solve_maze()
        self.write_output()

    def solve_maze(self):
        """Find the shortest path using BFS."""
        result = find_shortest_path_bfs(
            self.maze, self.entry, self.exit_end, self.width, self.height, self.block_42
        )
        if result:
            self.path, self.moves = result
        else:
            self.path, self.moves = [], 0

    def write_output(self):
        write_hex_output(
            self.maze,
            self.width,
            self.height,
            self.out_file,
            self.entry,
            self.exit_end,
            self.moves
        )

    def get_grid(self, show_path=False):
        """Return the grid as text for display."""
        return print_maze(
            self.maze,
            self.width,
            self.height,
            self.block_42,
            self.entry,
            self.exit_end,
            self.path if show_path else []
        )
