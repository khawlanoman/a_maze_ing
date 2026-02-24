from src.read_config import read_config
from src.grid import create_maze, create_block_42, print_maze, write_hex_output, write_visual_output
from src.algos import dfs
from src.algos import binary_tree, non_perfect

import time




if __name__ == "__main__":
    width, height, entry, exit_end, out_file, prefect = read_config()
    config = read_config()
    
    width = config["WIDTH"]
    height = config["HEIGHT"]
    entry = (config["ENTRY"][1],config["ENTRY"][0])
    exit_end = (config["EXIT"][1],config["EXIT"][0])
    out_file = config["OUTPUT_FILE"]
    prefect = True if config["PERFECT"] == "TRUE" else False

    maze = create_maze(width, height)

    blocK_42 = create_block_42(width, height)

    #binary_tree(maze, width, height, blocK_42)
    #if prefect == False:
    dfs(maze, width, height, start=entry, block_42=blocK_42)
    non_perfect(maze, width, height, blocK_42)
    grid1 = print_maze(maze, width, height, blocK_42, entry, exit_end)
   
    for line in grid1:
        #time.sleep(0.10)
        print(line)
    write_hex_output(maze, width, height)

    write_visual_output(grid1)



   