from .grid import create_maze, create_block_42
from .grid import print_maze, write_hex_output, Cell
from .algos import dfs, non_perfect, find_shortest_path_bfs
from typing import List


class MazeGenerator:
    def __init__(self, config: dict) -> None:
        self.width = int(config["WIDTH"])
        self.height = int(config["HEIGHT"])
        self.entry = tuple(config["ENTRY"])
        self.exit_end = tuple(config["EXIT"])
        self.out_file = config["OUTPUT_FILE"]
        self.perfect = str(config["PERFECT"]) in ["TRUE", 1]

        self.maze: list[list[Cell]]
        self.block_42: List = []
        self.path: List[tuple[int, int]] = []
        self.moves: List[str] = []

    def generate_maze(self) -> None:
        """Create a new maze and compute path."""
        self.maze = create_maze(self.width, self.height)
        self.block_42 = create_block_42(self.width, self.height,
                                        self.entry, self.exit_end)

        dfs(maze=self.maze, width=self.width, height=self.height,
            start=self.entry, block_42=self.block_42)

        if not self.perfect:
            non_perfect(maze=self.maze, width=self.width,
                        height=self.height, block_42=self.block_42)

        self.shortest_path()
        self.write_output()

    def shortest_path(self) -> None:
        """Find the shortest path using BFS."""
        result = find_shortest_path_bfs(
            self.maze, self.entry, self.exit_end,
            self.width, self.height, self.block_42
        )
        if result:
            self.path, self.moves = result
        else:
            self.path, self.moves = [], []

    def write_output(self) -> None:
        write_hex_output(
            maze=self.maze,
            width=self.width,
            height=self.height,
            out_file=self.out_file,
            entry=self.entry,
            exit_end=self.exit_end,
            moves=self.moves
        )

    def get_grid(self, show_path: bool = False) -> List:
        """Return the grid as text for display."""
        return print_maze(
            maze=self.maze,
            width=self.width,
            height=self.height,
            block_42=self.block_42,
            entry=self.entry,
            exit_end=self.exit_end,
            path=self.path if show_path else []
        )
