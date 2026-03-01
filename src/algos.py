import random
from collections import deque


def dfs(maze, width, height, start, block_42):
    """we need stack to know our path"""
    stack = [start]
    """we need visited to know the visited cells to don't visit them again"""
    visited = set()
    visited.add(start)

    while stack:
        current_r, current_c = stack[-1]
        neighbors = []
        directions = {'N': (-1, 0),
                      'S': (1, 0),
                      'E': (0, 1),
                      'W': (0, -1)}

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


def binary_tree(maze, width, height, blocK_42, entry, exit_end):
   
   
    current_r, current_c = entry

    while (current_r, current_c) != exit_end:
        next_r, next_c = current_r, current_c

       
        move_options = []
        if current_r < exit_end[0] and (current_r + 1, current_c) not in blocK_42:
            move_options.append('S')
        if current_c < exit_end[1] and (current_r, current_c + 1) not in blocK_42:
            move_options.append('E')

        if not move_options:
            
            if current_r < height - 1:
                move_options.append('S')
            if current_c < width - 1:
                move_options.append('E')

        chosen = random.choice(move_options)

        if chosen == 'S':
            maze[current_r][current_c].s = 0
            maze[current_r + 1][current_c].n = 0
            current_r += 1
        elif chosen == 'E':
            maze[current_r][current_c].e = 0
            maze[current_r][current_c + 1].w = 0
            current_c += 1

    
    for r in range(height):
        for c in range(width):

            if (r, c) in blocK_42 or (r, c) == entry or (r, c) == exit_end:
                continue

            directions = []

            if r > 0 and (r - 1, c) not in blocK_42:
                directions.append('N')

            if c < width - 1 and (r, c + 1) not in blocK_42:
                directions.append('E')

            if not directions:
                continue

            chosen = random.choice(directions)

            if chosen == 'N':
                maze[r][c].n = 0
                maze[r - 1][c].s = 0

            elif chosen == 'E':
                maze[r][c].e = 0
                maze[r][c + 1].w = 0






##################
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



""" this is BFS algorithm for finding the shortest possible way between 'ENTRY' and 'EXIT' """
def find_shortest_path_bfs(maze, start, end, width, height, block_42):
    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        current = queue.popleft()
        if current == end:
            break
        r, c = current
        if maze[r][c].n == 0 and (r-1, c) not in visited:
            if r-1 >= 0:
                visited.add((r-1, c))
                parent[(r-1, c)] = current
                queue.append((r-1, c))

        if maze[r][c].s == 0 and (r+1, c) not in visited:
            if r+1 < height:
                visited.add((r+1, c))
                parent[(r+1, c)] = current
                queue.append((r+1, c))

        if maze[r][c].e == 0 and (r, c+1) not in visited:
            if c+1 < width:
                visited.add((r, c+1))
                parent[(r, c+1)] = current
                queue.append((r, c+1))

        if maze[r][c].w == 0 and (r, c-1) not in visited:
            if c-1 >= 0:
                visited.add((r, c-1))
                parent[(r, c-1)] = current
                queue.append((r, c-1))

    if end not in parent and start != end:
        return []

    path = []
    node = end

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()
    directions = []
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]

        if r2 == r1 - 1:
            directions.append("N")
        elif r2 == r1 + 1:
            directions.append("S")
        elif c2 == c1 + 1:
            directions.append("E")
        elif c2 == c1 - 1:
            directions.append("W")

    return path, directions

    