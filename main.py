from src.read_config import read_config
from src.grid import create_maze, create_block_42, print_maze, write_hex_output
from src.algos import dfs
from src.algos import binary_tree, non_perfect, find_shortest_path_bfs # noqa
import time # q
import sys

import curses
import random

config = read_config()
width = config["WIDTH"]
height = config["HEIGHT"]
entry = tuple(config["ENTRY"])
exit_end = tuple(config["EXIT"])
out_file = config["OUTPUT_FILE"]
prefect = True if config["PERFECT"] == "TRUE" else False

maze = create_maze(width, height)

blocK_42 = create_block_42(width, height, entry, exit_end)
#binary_tree(maze, width, height, blocK_42, entry, exit_end)
#if prefect == False:
if prefect == True:
    dfs(maze, width, height, start=entry, block_42=blocK_42)
elif prefect == False:
    dfs(maze, width, height, start=entry, block_42=blocK_42)
    non_perfect(maze, width, height, blocK_42)
result = find_shortest_path_bfs(maze, entry, exit_end, width, height, blocK_42)
if result:
    path, moves = result
else:
    path, moves = [], 0

grid1 = print_maze(maze, width, height, blocK_42, entry, exit_end, path)

#print("PATH LENGTH:", len(path))
#print("PATH:", path)
#for line in grid1:
    #time.sleep(0.10)
#    print(line)
write_hex_output(maze, width, height, out_file, entry, exit_end, moves)

def main(stdscr, grid):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_MAGENTA)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

    blue_magenta= curses.color_pair(1)
    white_black= curses.color_pair(2)
    white_green= curses.color_pair(3)
    magenta_white= curses.color_pair(4)
    white_magenta= curses.color_pair(7)
    red_yellow   = curses.color_pair(5)
    red_black    = curses.color_pair(6)

    colors =[blue_magenta,
             white_black,
             white_green,
             magenta_white,
             white_magenta,
             red_yellow,
             red_black]

    maze_colors = random.randint(1, len(colors))
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        
        for row, line in enumerate(grid):
            if row >= height:
                break
            
            stdscr.addstr(row, 6, line[:width - 1], curses.color_pair(maze_colors))



        stdscr.addstr( row + 10, 5,"1. Re-generate a new maze")
        stdscr.addstr( row + 10,35 ,"2. Show / Hide path from entry to exit")
        stdscr.addstr( row + 11, 5,"3. Rotate maze colors")
        stdscr.addstr( row + 11, 35,"4. Quit")

        key = stdscr.getch()

        index = maze_colors
        stdscr.refresh()

        if key == ord('3'):
            maze_colors = random.randint(1, len(colors))
            while index == maze_colors:
                maze_colors = random.randint(1, len(colors))
            index = maze_colors


        if key == ord('4'):
            sys.exit(1)
        
                
curses.wrapper(lambda stdscr: main(stdscr, grid1))
