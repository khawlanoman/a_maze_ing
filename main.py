from src.cell import Cell
from src.read_config import read_config
from src.grid import create_maze, create_block_42, binary_tree, print_maze, write_hex_output, write_visual_output

if __name__ == "__main__":
    width, height, entry, exit_end, out_file, prefect = read_config()

    maze = create_maze(width, height)

    blocK_42 = create_block_42(width, height)

    binary_tree(maze, width, height, blocK_42)

    grid1 = print_maze(maze, width, height, blocK_42, entry, exit_end)
    for line in grid1:
        print(line)
    write_hex_output(maze, width, height)

    write_visual_output(grid1)



   