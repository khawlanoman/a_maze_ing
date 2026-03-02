# ===================== CELL =====================

class Cell:
    def __init__(self):
        self.n = 1
        self.e = 1
        self.s = 1
        self.w = 1

# ===================== MAZE =====================


def create_maze(width, height):
    maze = [[Cell() for _ in range(width)] for _ in range(height)]

    for r in range(height):
        for c in range(width):
            cell = maze[r][c]

            if r == 0:
                cell.n = 1
            if r == height - 1:
                cell.s = 1
            if c == 0:
                cell.w = 1
            if c == width - 1:
                cell.e = 1

    return maze


# ===================== 42 BLOCK =====================

def create_block_42(width, height, entry, exit_end):

    if width <= 8 or height <= 6:
        return []

    bh, bw = 5, 7
    y = (height // 2) - (bh // 2)
    x = (width // 2) - (bw // 2)

    block_42 = [
        (y, x), (y, x+4), (y, x+5), (y, x+6),
        (y+1, x), (y+1, x+6),
        (y+2, x), (y+2, x+1), (y+2, x+2),
        (y+2, x+4), (y+2, x+5), (y+2, x+6),
        (y+3, x+2), (y+3, x+4),
        (y+4, x+2), (y+4, x+4), (y+4, x+5), (y+4, x+6)
    ]

    if entry in block_42 or exit_end in block_42:
        print("Error: ENTRY or EXIT overlaps 42 block!")
        exit(1)

    return block_42


# ===================== PRINT MAZE =====================

def print_maze(maze, width, height, block_42, entry, exit_end, path):

    cell_width = 3
    output = []

    for r in range(height):

        # Top wall
        top = "█"
        for c in range(width):
            top += ("█" * cell_width if maze[r][c].n else " " * cell_width) + "█"
        output.append(top)

        # Cell content
        row_line = "█"

        for c in range(width):

            if (r, c) in block_42:
                content = "   "
            elif (r, c) == entry:
                content = " S "
            elif (r, c) == exit_end:
                content = " E "
            elif path and (r, c) in path:
                content = " ➡ "
            else:
                content = " " * cell_width

            row_line += content
            row_line += "█" if c == width - 1 or maze[r][c].e else " "

        output.append(row_line)

    # Bottom wall
    bottom = "█" + ("█" * cell_width + "█") * width
    output.append(bottom)

    return output


# ===================== HEX OUTPUT =====================

def cell_to_hex(cell):
    return format(
        cell.n * 1 +
        cell.e * 2 +
        cell.s * 4 +
        cell.w * 8,
        "X"
    )


def write_hex_output(maze, width, height, out_file, entry, exit_end, moves):

    with open(out_file, "w") as f:

        for r in range(height):
            f.write("".join(cell_to_hex(maze[r][c]) for c in range(width)) + "\n")

        f.write(f"\n{entry[0]},{entry[1]}\n")
        f.write(f"{exit_end[0]},{exit_end[1]}\n")
        f.write("".join(moves))