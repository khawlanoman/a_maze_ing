from .cell import Cell
import random

GREEN = "\033[42m"  
RED = "\033[41m"  
RESET = "\033[0m" 

def create_maze(width, height):
    maze = [[Cell() for c in range(width)] for r in range(height)]

    gird_tab = []

    for c in range(height):
        row = []
        for r in range(width):
            cell = maze[c][r]

            if r == 0:
                cell.n = 1
            if r == height - 1:
                cell.s = 1
            if c == 0:
                cell.w = 1
            if c == width -1:
                cell.e = 1

            row.append(cell)

        gird_tab.append(row)

    return maze

def create_block_42(width, height):
    if width <= 8 or height <= 6:
        return []
    block_height = 5
    block_width = 7

    y = (height // 2) - (block_height // 2)
    x = (width // 2) - (block_width // 2)

    blocK_42 = [
        (y, x),(y, x + 4),(y, x + 5),(y, x + 6),
        (y+1,x),(y+1,x + 6),
        (y+2,x),(y+2,x+1),(y+2,x+2),(y+2,x+4),(y+2,x+5),(y+2,x+ 6),
        (y+3,x+2),(y+3, x+4),
        (y+4, x+2),(y+4, x +4),(y+4, x+5),(y+4, x +6)
    ]

    return blocK_42


def print_maze(maze, width, height, blocK_42, entry, exit_end):

    cell_width = 3
    cell_height = 1

    grid1 = []

    for r in range(height):
    
        top_row = "█"
        for c in range(width):
            if maze[r][c].n:       
                top_row += "█" * cell_width
            else:
                top_row += " " * cell_width
            top_row += "█"
        grid1.append(top_row)

    
        for h in range(cell_height):
            row = "█"  
            for c in range(width):
                if (r, c) in blocK_42:
                    content = f"{GREEN}   {RESET}"
                elif (r, c) == entry:
                    content = f"{GREEN}   {RESET}"
                elif (r, c) == exit_end:
                    content = f"{RED}   {RESET}"
                else:
                    content = " " * cell_width

                row += content

            
                if c == width - 1 or maze[r][c].e:
                    row += "█"
                else:
                    row += " "
            grid1.append(row)

    bottom_row = "█"
    for c in range(width):
        bottom_row += "█" * cell_width + "█"
    grid1.append(bottom_row)

    return (grid1)




def cell_to_hex(cell):
    value = 0
    value += cell.n * 1
    value += cell.e * 2
    value += cell.s * 4
    value += cell.w * 8
    return format(value, 'x')


def write_hex_output(maze, width, height):
    file = open("output_maze.txt","w")
    for c in range(height):
        line =  ""
        for r in range(width):
            line += cell_to_hex(maze[c][r])
        file.write(line +"\n")


def write_visual_output(grid1):
    with open("maze.txt", "w") as file:
        for row in grid1:
            file.write(''.join(row))
            file.write('\n')