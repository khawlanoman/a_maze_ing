import curses


def main(stdscr):
    stdscr.addstr(5, 5, "Press any key...")
    stdscr.refresh()
    key = stdscr.getch()
    stdscr.addstr(7, 5, f"You pressed: {key}")
    stdscr.refresh()
    stdscr.getch()
    curses.wrapper(main)
