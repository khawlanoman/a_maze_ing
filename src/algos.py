import random

def dfs(maze, width, height, start, block_42):
    stack = [start]
    visited = set()
    visited.add(start)

    while stack:
        current_r, current_c = stack[-1]

        neighbors = []
        directions = {'N': (-1,0),
                      'S': (1,0),
                      'E':(0,1),
                      'W':(0,-1)}

        for direction, (r_offset, c_offset) in directions.items():
            neighbor_r = current_r + r_offset
            neighbor_c = current_c + c_offset

            if 0 <= neighbor_r < height and 0 <= neighbor_c < width:
                if (neighbor_r, neighbor_c) not in visited and (neighbor_r, neighbor_c) not in block_42:
                    neighbors.append((direction, (neighbor_r, neighbor_c)))

        if neighbors:
            direction, (neighbor_r, neighbor_c) = random.choice(neighbors)


            if direction == 'N':
                maze[current_r][current_c].n = 0
                maze[neighbor_r][neighbor_c].s = 0

            elif direction == 'S':
                maze[current_r][current_c].s = 0
                maze[neighbor_r][neighbor_c].n = 0

            elif direction == 'E':
                maze[current_r][current_c].e = 0
                maze[neighbor_r][neighbor_c].w = 0

            elif direction == 'W':
                maze[current_r][current_c].w = 0
                maze[neighbor_r][neighbor_c].e = 0

            visited.add((neighbor_r, neighbor_c))
            stack.append((neighbor_r, neighbor_c))
        else:
            stack.pop()



def binary_tree(maze, width, height, blocK_42):
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
                    if (r,c) not in blocK_42 and (r -1, c) not in blocK_42:
                        maze[r][c].n = 0
                        maze[r - 1][c].s = 0

                elif chosen == 'E':
                    if (r,c) not in blocK_42 and (r, c + 1) not in blocK_42:
                        maze[r][c].e = 0
                        maze[r][c + 1].w = 0



def non_perfect(maze, width, height, blocK_42):

    extra_break = (width * height) // 3

    for i in range(extra_break):

            r = random.randint(0, height - 1)
            c = random.randint(0, width - 1)

            if (r, c) in blocK_42:
                continue
            
            direction = []

            if r > 0:
                direction.append('N')
            if c < width -1:
                direction.append('E')
            if r < height -1:
                direction.append('S')
            if c > 0:
                direction.append('W')

            if not direction:
                continue
                
            chosen = random.choice(direction)

            if chosen == 'N' and (r - 1, c) not in blocK_42:
                if (r,c) not in blocK_42 and (r -1, c) not in blocK_42:
                    maze[r][c].n = 0
                    maze[r - 1][c].s = 0

            elif chosen == 'E' and (r, c + 1) not in blocK_42:
                if (r,c) not in blocK_42 and (r, c + 1) not in blocK_42:
                    maze[r][c].e = 0
                    maze[r][c + 1].w = 0
            
            elif chosen == 'S' and (r + 1, c) not in blocK_42:
                if (r,c) not in blocK_42 and (r, c + 1) not in blocK_42:
                    maze[r][c].s = 0
                    maze[r + 1][c].n = 0
            
            elif chosen == 'E' and (r, c - 1) not in blocK_42:
                if (r,c) not in blocK_42 and (r, c + 1) not in blocK_42:
                    maze[r][c].w = 0
                    maze[r][c - 1].e = 0

