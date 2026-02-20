import random


class Cell:
    def __init__(self):
        self.n = 1
        self.e = 1
        self.s = 1
        self.w = 1

#width = int(input("enter Width:"))
#height = int(input("enter height:"))

with open("config.txt","r") as file:
    
    array= {}
    for line in file:
        key, value = line.strip().split("=")
        array[key] = value



for key, value in array.items() :
    if key == "WIDTH":
        width = int(value)
    elif key == "HEIGHT":
        height = int(value)
    elif key == "ENTRY":
        entry = tuple(value)
    elif key == "EXIT":
        exit_end = tuple(map(int ,value.split(",")))
        print(exit_end)
    elif key == "OUTPUT_FILE":
        out_file = str(value)
    elif key == "PERFECT":
        prefect = bool(value)
#gird_tab = [[random.choice(['.', '#']) for h in range(height)] for w in range(width)]
print(array)
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

grid = []

#top = ["▄▄"] * (width)
#top.pop() 
#grid.append(top)


top_row = ["▄"]
for r in range(width):

    if maze[0][r].n == 1:
        top_row.append("▄▄")
   
grid.append(top_row)
for c in  range(height):

    row = []
    row.append("█")
    for r in range(width):
        
        cell = maze[c][r]
       
        if cell.n == 1:
            
            row.append("▄")
        else:
             row.append(" ")
       # if cell.w == 1:
          #  row.append("█")
        if cell.e == 1:
            row.append("█")
        else:
            row.append(" ")
        #if cell.s == 1:
          #  continue
    grid.append(row)

for i in grid:
        print("".join(i))

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

#█ ▄
with open("maze.txt", "w") as file:
    for row in grid:
       file.write(''.join(row))
       file.write('\n')

