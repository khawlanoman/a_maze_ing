from src.read_config import read_config
from src.grid import create_maze, create_block_42, print_maze, write_hex_output
from src.algos import dfs
from src.algos import binary_tree, non_perfect, find_shortest_path_bfs # noqa
import time # noqa
import sys # noqa

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
# binary_tree(maze, width, height, blocK_42, entry, exit_end)
# if prefect == False:
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

# print("PATH LENGTH:", len(path))
# print("PATH:", path)
# for line in grid1:
# time.sleep(0.10)
#    print(line)
write_hex_output(maze, width, height, out_file, entry, exit_end, moves)


def main(stdscr, grid):
    curses.curs_set(0)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_MAGENTA)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

    colors = [1, 2, 3, 4, 5, 6, 7]
    maze_color = random.choice(colors)

    while True:
        stdscr.clear()
        term_height, term_width = stdscr.getmaxyx()

        # ----- Minimum required size -----
        required_height = len(grid) + 4
        required_width = max(len(line) for line in grid) + 8

        if term_height < required_height or term_width < required_width:
            warning = "Terminal too small. Please resize."
            stdscr.addstr(0, 0, warning[:term_width - 1])
            stdscr.refresh()
            stdscr.getch()
            continue

        # ----- Draw Maze -----
        for row, line in enumerate(grid):
            if row >= term_height:
                break

            max_x = term_width - 6 - 1
            if max_x <= 0:
                continue

            try:
                stdscr.addstr(row, 6, line[:max_x], curses.color_pair(maze_color))
            except curses.error:
                pass

        # ----- Draw Menu -----
        menu_y = min(len(grid) + 2, term_height - 3)

        try:
            stdscr.addstr(menu_y, 5, "1. Re-generate a new maze")
            stdscr.addstr(menu_y, 35, "2. Show / Hide path from entry to exit")
            stdscr.addstr(menu_y + 1, 5, "3. Rotate maze colors")
            stdscr.addstr(menu_y + 1, 35, "4. Quit")
        except curses.error:
            pass

        stdscr.refresh()
        key = stdscr.getch()

        # ----- Handle Input -----
        if key == ord('3'):
            new_color = random.choice(colors)
            while new_color == maze_color:
                new_color = random.choice(colors)
            maze_color = new_color

        elif key == ord('4'):
            break


curses.wrapper(lambda stdscr: main(stdscr, grid1))
