import random

class Cell():
    def __init__(self):
        n = 1
        e = 1
        s = 1
        w = 1

#width = int(input("enter Width:"))
#height = int(input("enter height:"))

with open("config.txt","r") as file:
    
    array= {}
    for line in file:
        key, value = line.strip().split("=")
        array[key] = value
print(array)

for key, value in array.items() :
    if key == "WIDTH":
        width = int(value)
    elif key == "HEIGHT":
        height = int(value)
#gird_tab = [[random.choice(['.', '#']) for h in range(height)] for w in range(width)]
cell_wall = Cell()
gird_tab = []
for c in range(height):
    row = []
    for r in range(width):
        cell = random.choice(['.', '#'])
        row.append(cell)
    gird_tab.append(row)


with open("maze.txt", "w") as file:
    for row in gird_tab:
        file.write(' '.join(row))
        file.write('\n')
