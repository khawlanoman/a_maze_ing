from src.read_config import read_config
from src.grid import create_maze, create_block_42, print_maze, write_hex_output
from src.algos import dfs
from src.algos import non_perfect, find_shortest_path_bfs  # noqa
import time
import curses
import random


# -------------------- CONFIG --------------------

config = read_config()

width = config["WIDTH"]
height = config["HEIGHT"]
entry = tuple(config["ENTRY"])
exit_end = tuple(config["EXIT"])
out_file = config["OUTPUT_FILE"]
perfect = True if config["PERFECT"] == "TRUE" else False


# -------------------- INITIAL MAZE --------------------

maze = create_maze(width, height)
blocK_42 = create_block_42(width, height, entry, exit_end)

if perfect:
    dfs(maze, width, height, start=entry, block_42=blocK_42)
elif not perfect:
    dfs(maze, width, height, start=entry, block_42=blocK_42)
    non_perfect(maze, width, height, blocK_42)

result = find_shortest_path_bfs(maze, entry, exit_end, width, height, blocK_42)
if result:
    path, moves = result
else:
    path, moves = [], 0

grid1 = print_maze(maze, width, height, blocK_42, entry, exit_end, path)

write_hex_output(
    maze,
    width,
    height,
    out_file,
    entry,
    exit_end,
    moves
)

##############################3
def animate_path(stdscr, path, start_x, entry, exit_end):

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

        #stdscr.refresh()
        #curses.napms(30)
        prev = current
# -------------------- CURSES UI --------------------

def main(stdscr):

    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors() 

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
    #_, maze_bg = curses.pair_content(maze_color)
    
    color_path = 9
    
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
        time.sleep(1)

    # ---------- Maze Generation ----------

    def generate_maze():

        nonlocal maze, blocK_42, path, moves

        maze = create_maze(width, height)

        blocK_42 = create_block_42(width, height, entry, exit_end)

        dfs(maze, width, height, start=entry, block_42=blocK_42)

        if not perfect:
            non_perfect(maze, width, height, blocK_42)

        result = find_shortest_path_bfs(
            maze, entry, exit_end, width, height, blocK_42
        )

        if result:
            path, moves = result
        else:
            path, moves = [], 0

        write_hex_output(maze, width, height, out_file, entry, exit_end, moves)

    # ---------- Initial Setup ----------

    maze = None
    blocK_42 = None
    path = []
    moves = 0
    generate_maze()

    # ---------- Main Loop ----------
    flag = False
    flag1 = False
    while True:

        stdscr.clear()
        term_height, term_width = stdscr.getmaxyx()
        ##################################
        if maze_color == 1 or maze_color == 2 or maze_color == 6:
            curses.init_pair(9, curses.COLOR_GREEN,curses.COLOR_BLACK)
            curses.init_pair(10, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
            curses.init_pair(11, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        elif maze_color == 3:
            curses.init_pair(9, curses.COLOR_RED, curses.COLOR_GREEN)
            curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_BLACK)
            curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_GREEN)
        elif maze_color == 4 or maze_color == 8:
            curses.init_pair(9, curses.COLOR_GREEN,curses.COLOR_WHITE)
            curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_BLACK)
            curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_WHITE)
        elif maze_color == 5 :
            curses.init_pair(9, curses.COLOR_GREEN,curses.COLOR_YELLOW)
            curses.init_pair(10, curses.COLOR_RED, curses.COLOR_RED)
            curses.init_pair(11, curses.COLOR_RED, curses.COLOR_YELLOW)
        elif maze_color == 7 :
            curses.init_pair(9, curses.COLOR_GREEN, curses.COLOR_MAGENTA)
            curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_BLACK)
            curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_MAGENTA)

           
        ################################
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
            
            start_x = max((term_width - len(line)) // 2, 0)
            
            for col, char in enumerate(line):
                current_x = start_x + col
                if current_x >= term_width - 6: # Stay within bounds
                    break

                # 1. Start with the default maze color
                use_color = curses.color_pair(maze_color)

                if char == "S" or char == "E":     
                    use_color = curses.color_pair(11)
              
                elif char == "*":      
                    use_color = curses.color_pair(10)
                
                if show_path and path:
                    animate_path(stdscr, path, start_x, entry, exit_end)
                    
                #elif show_path and char == "•":
                   # use_color = curses.color_pair(9)
                # 4. Draw the single character
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
            start_x = max((term_width - len(line)) // 2, 0)  # center horizontally
            try:
                stdscr.addstr(menu_y + i, start_x, line)
            except curses.error:
                pass

        stdscr.refresh()
       
        ###################
    
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
