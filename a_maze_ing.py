from mazegen.read_config import read_config
from mazegen.MazeGenerator import MazeGenerator
import time
import curses
import random
import sys
from typing import List, 


# -------------------- Path Animation --------------------
def animate_path(stdscr: "curses._CursesWindow", path: List[tuple[int, int]],
                 start_x: int, entry: tuple, exit_end: tuple) -> None:
    if not path:
        return

    prev = path[0]
    for current in path[1:]:
        y0, x0 = prev
        y1, x1 = current
        screen_y0 = y0 * 2 + 1
        screen_x0 = start_x + (x0 * 4 + 2)
        screen_y1 = y1 * 2 + 1
        screen_x1 = start_x + (x1 * 4 + 2)
        mid_y = (screen_y0 + screen_y1) // 2
        mid_x = (screen_x0 + screen_x1) // 2

        try:
            stdscr.addch(mid_y, mid_x, "•", curses.color_pair(9))
            if (y1, x1) != entry and (y1, x1) != exit_end:
                stdscr.addch(screen_y1, screen_x1, "•", curses.color_pair(9))
        except curses.error:
            pass

        prev = current


try:
    config = read_config()
    maze_gen = MazeGenerator(config)
    maze_gen.generate_maze()
except Exception as e:
    print(f"[ERROR] {e}")
    sys.exit(1)


# -------------------- Main Curses UI ------------;--------

def main(stdscr):

    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    # Base colors
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(8, curses.COLOR_CYAN, curses.COLOR_WHITE)
    colors = [1, 2, 3, 4, 5, 6, 7, 8]
    maze_color = random.choice(colors)
    show_path = False
    flag = False
    flag1 = False
    # ---------- A-maze-ing Logo ----------

    def show_amazeing(stdscr):
        stdscr.clear()
        art = [
            " █████╗    ███╗   ███╗ █████╗ ███████╗ ███████╗   ██╗███╗   ██╗ ██████╗ ", # noqa
            "██╔══██╗   ████╗ ████║██╔══██╗╚══███╔╝ ██╔════╝   ██║████╗  ██║██╔════╝ ", # noqa
            "███████║   ██╔████╔██║███████║  ███╔╝  █████╗     ██║██╔██╗ ██║██║  ███╗", # noqa
            "██╔══██║   ██║╚██╔╝██║██╔══██║ ███╔╝   ██╔══╝     ██║██║╚██╗██║██║   ██║", # noqa
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
        time.sleep(1)
    while True:
        stdscr.clear()
        term_height, term_width = stdscr.getmaxyx()
        # Set maze-specific color pairs
        if maze_color in [1, 2, 6]:
            curses.init_pair(9, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(10, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
            curses.init_pair(11, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        elif maze_color == 3:
            curses.init_pair(9, curses.COLOR_RED, curses.COLOR_GREEN)
            curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_BLACK)
            curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_GREEN)
        elif maze_color in [4, 8]:
            curses.init_pair(9, curses.COLOR_GREEN, curses.COLOR_WHITE)
            curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_BLACK)
            curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_WHITE)
        elif maze_color == 5:
            curses.init_pair(9, curses.COLOR_GREEN, curses.COLOR_YELLOW)
            curses.init_pair(10, curses.COLOR_RED, curses.COLOR_RED)
            curses.init_pair(11, curses.COLOR_RED, curses.COLOR_YELLOW)
        elif maze_color == 7:
            curses.init_pair(9, curses.COLOR_GREEN, curses.COLOR_MAGENTA)
            curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_BLACK)
            curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
        # Show logo once
        if not flag:
            show_amazeing(stdscr)
            flag = True
            stdscr.clear()
        grid = maze_gen.get_grid(show_path)
        required_height = len(grid) + 4
        required_width = max(len(line) for line in grid) + 8
        if term_height < required_height or term_width < required_width:
            warning = "Terminal too small. Please resize."
            stdscr.addstr(0, 0, warning[:term_width - 1])
            stdscr.refresh()
            stdscr.getch()
            continue
        # Draw maze
        for row, line in enumerate(grid):
            if row >= term_height:
                break
            start_x = max((term_width - len(line)) // 2, 0)
            for col, char in enumerate(line):
                current_x = start_x + col
                if current_x >= term_width - 6:
                    break
                use_color = curses.color_pair(maze_color)
                if char in ["S", "E"]:
                    use_color = curses.color_pair(11)
                elif char == "*":
                    use_color = curses.color_pair(10)
                if show_path and maze_gen.path:
                    animate_path(stdscr, maze_gen.path, start_x,
                                 maze_gen.entry, maze_gen.exit_end)
                try:
                    stdscr.addch(row, current_x, char, use_color)
                except curses.error:
                    pass
                if not flag1:
                    stdscr.refresh()
                    curses.napms(3)

        # ---------- Menu ----------
        flag1 = True
        menu_y = min(len(grid) + 2, term_height - 3)
        menu_lines = [
            "[1]. Re-generate a new maze     [2]. Show / Hide path",
            "[3]. Rotate maze colors         [4]. Quit"
        ]
        for i, line in enumerate(menu_lines):
            start_x = max((term_width - len(line)) // 2, 0)
            try:
                stdscr.addstr(menu_y + i, start_x, line)
            except curses.error:
                pass
        stdscr.refresh()
        key = stdscr.getch()
        # ---------- Inputs ----------
        if key == ord('1'):
            maze_gen.generate_maze()
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

try:
    curses.wrapper(main)
except KeyboardInterrupt:
    print("Program interrupted by user.")
