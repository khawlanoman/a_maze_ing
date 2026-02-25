import random

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'


class Cell:
    def __init__(self):
        self.n = 1
        self.e = 1
        self.s = 1
        self.w = 1
        #self.blocK_42 = False


with open("config.txt","r") as file:
    array = {}
    for line in file:
        key, value = line.strip().split("=")
        array[key] = value

for key, value in array.items() :
    if key == "WIDTH":
        width = int(value)
    elif key == "HEIGHT":
        height = int(value)
    elif key == "ENTRY":
        entry = tuple(int(i.strip()) for i in value.split(","))
    elif key == "EXIT":
        exit_end = tuple(int(i.strip()) for i in value.split(","))
        print(exit_end)
    elif key == "OUTPUT_FILE":
        out_file = str(value)
    elif key == "PERFECT":
        prefect = bool(value)

gird_tab = []

maze = [[Cell() for c in range(width)] for r in range(height)]

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

############################
block_height = 5
block_width = 7

y =( height // 2) - ( block_height // 2)
x =( width // 2) - (block_width // 2)
blocK_42 = [(y, x),( y, x + 4), (y, x + 5), (y, x + 6),
            (y + 1 ,x), (y + 1,x + 6),
            (y+2, x), (y+2, x+1), (y+2, x+2), (y+2, x+4), (y+2 ,x+5), (y+2,x+ 6),
            (y+3, x+2), (y+3, x+4),
            (y+4, x + 2), (y + 4, x + 4), (y + 4, x + 5), (y + 4, x + 6)
]



############################
for r in range(height):

    for c in range(width):
        direction = []

        if r > 0:
            direction.append('N')
        if c < width -1:
            direction.append('E')

        if direction:
            chosen = random.choice(direction)
            if chosen == 'N':
                if(r,c) not in blocK_42 and (r -1, c) not in blocK_42:
                    maze[r][c].n = 0
                    maze[r - 1][c].s = 0
            elif chosen == 'E':
                if(r,c) not in blocK_42 and (r, c + 1) not in blocK_42:
                    maze[r][c].e = 0
                    maze[r][c + 1].w = 0



#########################################
"""
def remove_wall(maze, r, c, nr, nc, direction):

    if direction == "N":
        maze[r][c].n = False
        maze[nr][nc].s = False

    elif direction == "S":
        maze[r][c].s = False
        maze[nr][nc].n = False

    elif direction == "E":
        maze[r][c].e = False
        maze[nr][nc].w = False

    elif direction == "W":
        maze[r][c].w = False
        maze[nr][nc].e = False



def aldous_broder(maze, width, height, block_42):

    total_cells = width * height - len(block_42)

    while True:
        r = random.randint(0, height - 1)
        c = random.randint(0, width - 1)
        if (r, c) not in block_42:
            break

    visited = set()
    visited.add((r, c))
    visited_count = 1

    current = (r, c)

    while visited_count < total_cells:

        r, c = current

        neighbors = []

        directions = {
            "N": (-1, 0),
            "S": (1, 0),
            "E": (0, 1),
            "W": (0, -1)
        }

        for direction, (dr, dc) in directions.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width:
                if (nr, nc) not in block_42:
                    neighbors.append((direction, nr, nc))

        direction, nr, nc = random.choice(neighbors)

        if (nr, nc) not in visited:
            remove_wall(maze, r, c, nr, nc, direction)
            visited.add((nr, nc))
            visited_count += 1

        current = (nr, nc)
"""
#for r in range(center_r, center_r + block_height):
#    for c in range(center_c, center_c + block_width):
#        maze[r][c].n = 1
#        maze[r][c].e = 1
#        maze[r][c].s = 1
#        maze[r][c].w = 1
#        maze[r][c].blocK_42 = True


"""
grid1 = []
for r in range(height):
    
    top_row = "█"
    for c in range(width):
        if maze[r][c].n == 1:
            top_row += "████"
        else:
            top_row += "   "
    
    grid1.append(top_row)

   
    row = "█"
    for c in range(width):
        if (r, c) == exit_end:
            content = " E "
        elif (r, c) == entry:
            content = " S "
        else:
            content = "   "
       
        row += content
        if c == width - 1 or maze[r][c].e == 1 :
            row += "█"
        else:
            row += " "
           

    grid1.append(row)


bottom_row = "█"
for c in range(width):
    bottom_row += "████"
grid1.append(bottom_row)


for i in grid1:
     print("".join(i))
"""
"""
grid1 = []

for r in range(height):
    # Top wall row
    top_row = "+"
    for c in range(width):
        if maze[r][c].n == 1:
            top_row += "---+"
        else:
            top_row += "   +"
    grid1.append(top_row)

    # Content row
    row = "|"
    for c in range(width):
        if(r,c)  in blocK_42:
            row +="███"
        elif (r,c) == entry:
            row += " S "
        elif (r,c) == exit_end:
            row += " E "
        else:
            row += "   "

        if c == width - 1 or maze[r][c].e == 1:
            row += "|"
        else:
            row += " "
    grid1.append(row)


bottom_row = "+"
for c in range(width):
    bottom_row += "---+"
grid1.append(bottom_row)


for line in grid1:
    print(line)

"""
#################

GREEN = "\033[42m"  
RED = "\033[41m"  
RESET = "\033[0m" 

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
                content = f"{GREEN}***{RESET}"
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


for line in grid1:
    print(line)
#################################

def cell_to_hex(cell):
    value = 0
    value += cell.n * 1
    value += cell.e * 2
    value += cell.s * 4
    value += cell.w * 8
    return format(value, 'x')


file = open("output_maze.txt","w")
for c in range(height):
    line =  ""
    for r in range(width):
        line += cell_to_hex(maze[c][r])
    file.write(line +"\n")


with open("maze.txt", "w") as file:
    for row in grid1:
       file.write(''.join(row))
       file.write('\n')

