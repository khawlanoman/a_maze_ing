from src.read_config import read_config
from src.grid import create_maze, create_block_42, print_maze, write_hex_output
from src.algos import dfs
from src.algos import binary_tree, non_perfect, find_shortest_path_bfs  # noqa
import time  # noqa
import sys  # noqa

import curses
import random


# -------------------- CONFIG --------------------

config = read_config()

width = config["WIDTH"]
height = config["HEIGHT"]
entry = tuple(config["ENTRY"])
exit_end = tuple(config["EXIT"])
out_file = config["OUTPUT_FILE"]
prefect = True if config["PERFECT"] == "TRUE" else False


# -------------------- INITIAL MAZE --------------------

maze = create_maze(width, height)

blocK_42 = create_block_42(width, height, entry, exit_end)

if prefect == True:
    dfs(maze, width, height, start=entry, block_42=blocK_42)

elif prefect == False:
    dfs(maze, width, height, start=entry, block_42=blocK_42)
    non_perfect(maze, width, height, blocK_42)

result = find_shortest_path_bfs(
    maze, entry, exit_end, width, height, blocK_42
)

if result:
    path, moves = result
else:
    path, moves = [], 0

grid1 = print_maze(
    maze,
    width,
    height,
    blocK_42,
    entry,
    exit_end,
    path
)

write_hex_output(
    maze,
    width,
    height,
    out_file,
    entry,
    exit_end,
    moves
)


# -------------------- CURSES UI --------------------

def main(stdscr):

    curses.curs_set(0)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_MAGENTA)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(8, curses.COLOR_CYAN, curses.COLOR_WHITE)

    colors = [1, 2, 3, 4, 5, 6, 7, 8]
    maze_color = random.choice(colors)

    show_path = False

    # ---------- Design A-maze-ing --------
    def show_amazeing(stdscr):
        stdscr.clear()

        art = [
            " █████╗    ███╗   ███╗ █████╗ ███████╗ ███████╗   ██╗███╗   ██╗ ██████╗ ", # noqa
            "██╔══██╗   ████╗ ████║██╔══██╗╚══███╔╝ ██╔════╝   ██║████╗  ██║██╔════╝ ", # noqa
            "███████║   ██╔████╔██║███████║  ███╔╝  █████╗     ██║██╔██╗ ██║██║  ███╗", # noqa
            "██╔══██║   ██║╚██╔╝██║██╔══██║ ███╔╝   ██╔══╝     ██║██║╚██╗██║██║   ██║",  # noqa
            "██║  ██║   ██║ ╚═╝ ██║██║  ██║███████  ███████╗   ██║██║ ╚████║╚██████╔╝", # noqa
            "╚═╝  ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚══════╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ " # noqa
        ]

        h, w = stdscr.getmaxyx()
        start_y = h // 2 - len(art) // 2
        for i, line in enumerate(art):
            x = w // 2 - len(line) // 2
            if 0 <= start_y + i < h:
                stdscr.addstr(start_y + i, max(0, x), line)

        stdscr.refresh()
        time.sleep(2)

    # ---------- Maze Generation ----------

    def generate_maze():

        nonlocal maze, blocK_42, path, moves

        maze = create_maze(width, height)

        blocK_42 = create_block_42(width, height, entry, exit_end)

        dfs(maze, width, height, start=entry, block_42=blocK_42)

        if not prefect:
            non_perfect(maze, width, height, blocK_42)

        result = find_shortest_path_bfs(
            maze, entry, exit_end, width, height, blocK_42
        )

        if result:
            path, moves = result
        else:
            path, moves = [], 0

        write_hex_output(
            maze,
            width,
            height,
            out_file,
            entry,
            exit_end,
            moves
        )

    # ---------- Initial Setup ----------

    maze = None
    blocK_42 = None
    path = []
    moves = 0
    generate_maze()

    # ---------- Main Loop ----------
    flag = False
    while True:

        stdscr.clear()
        term_height, term_width = stdscr.getmaxyx()

        if not flag:
            show_amazeing(stdscr)
            flag = True
            stdscr.clear()

        grid = print_maze(
            maze,
            width,
            height,
            blocK_42,
            entry,
            exit_end,
            path if show_path else []
        )

        required_height = len(grid) + 4
        required_width = max(len(line) for line in grid) + 8

        if term_height < required_height or term_width < required_width:

            warning = "Terminal too small. Please resize."

            stdscr.addstr(0, 0, warning[:term_width - 1])
            stdscr.refresh()
            stdscr.getch()

            continue

        # ---------- Draw Maze ----------

        for row, line in enumerate(grid):
            if row >= term_height:
                break

            max_x = term_width - 6 - 1
            if max_x <= 0:
                continue
            try:
                stdscr.addstr(
                    row,
                    6,
                    line[:max_x],
                    curses.color_pair(maze_color)
                )
                
            except curses.error:
                pass

        # ---------- Menu ----------

        menu_y = min(len(grid) + 2, term_height - 3)

        try:
            stdscr.addstr(menu_y, 5, "[1]. Re-generate a new maze")
            stdscr.addstr(menu_y, 35, "[2]. Show / Hide path")
            stdscr.addstr(menu_y + 1, 5, "[3]. Rotate maze colors")
            stdscr.addstr(menu_y + 1, 35, "[4]. Quit")
        except curses.error:
            pass

        stdscr.refresh()
        key = stdscr.getch()

        # ---------- Inputs ----------

        if key == ord('1'):
            generate_maze()

        elif key == ord('2'):
            show_path = not show_path

        elif key == ord('3'):
            new_color = random.choice(colors)

            while new_color == maze_color:
                new_color = random.choice(colors)

            maze_color = new_color

        elif key == ord('4'):
            break


# -------------------- RUN PROGRAM --------------------

curses.wrapper(main)
