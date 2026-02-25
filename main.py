from src.read_config import read_config
from src.grid import create_maze, create_block_42, print_maze, write_hex_output, write_visual_output
from src.algos import dfs
from src.algos import binary_tree, non_perfect, find_shortest_path_bfs # noqa
import time # noqa


if __name__ == "__main__":
    config = read_config()
    width = config["WIDTH"]
    height = config["HEIGHT"]
    entry = tuple(config["ENTRY"])
    exit_end = tuple(config["EXIT"])
    out_file = config["OUTPUT_FILE"]
    prefect = True if config["PERFECT"] == "TRUE" else False

    maze = create_maze(width, height)

    blocK_42 = create_block_42(width, height)

    #binary_tree(maze, width, height, blocK_42)
    #if prefect == False:
    dfs(maze, width, height, start=entry, block_42=blocK_42)
    #non_perfect(maze, width, height, blocK_42)
    path = find_shortest_path_bfs(maze, entry, exit_end, width, height, blocK_42)
    grid1 = print_maze(maze, width, height, blocK_42, entry, exit_end)

    print("PATH LENGTH:", len(path))
    print("PATH:", path)
    for line in grid1:
        #time.sleep(0.10)
        print(line)
    write_hex_output(maze, width, height)

    write_visual_output(grid1, out_file)
