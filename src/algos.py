import random
from collections import deque


# ==========================================================
# CENTRALIZED DIRECTIONS
# (row_offset, col_offset, current_wall, neighbor_wall)
# ==========================================================
DIRECTIONS = {
    'N': (-1, 0, 'n', 's'),
    'S': (1, 0, 's', 'n'),
    'E': (0, 1, 'e', 'w'),
    'W': (0, -1, 'w', 'e')
}


# ==========================================================
# HELPER: Break wall between two cells
# ==========================================================
def break_wall(maze, r, c, direction):
    dr, dc, wall, opposite = DIRECTIONS[direction]
    nr, nc = r + dr, c + dc

    setattr(maze[r][c], wall, 0)
    setattr(maze[nr][nc], opposite, 0)

    return nr, nc


# ==========================================================
# DFS MAZE GENERATION (Perfect Maze)
# ==========================================================
def dfs(maze, width, height, start, block_42):
    stack = [start]
    visited = {start}

    while stack:
        r, c = stack[-1]
        neighbors = []

        for direction, (dr, dc, _, _) in DIRECTIONS.items():
            nr, nc = r + dr, c + dc

            if (0 <= nr < height and
                0 <= nc < width and
                (nr, nc) not in visited and
                (nr, nc) not in block_42):
                neighbors.append(direction)

        if neighbors:
            chosen = random.choice(neighbors)
            nr, nc = break_wall(maze, r, c, chosen)

            visited.add((nr, nc))
            stack.append((nr, nc))
        else:
            stack.pop()


# ==========================================================
# BINARY TREE MAZE GENERATION
# ==========================================================
def binary_tree(maze, width, height, block_42, entry, exit_end):

    r, c = entry

    # Create guaranteed path from entry to exit
    while (r, c) != exit_end:
        moves = []

        if r < exit_end[0] and (r + 1, c) not in block_42:
            moves.append('S')

        if c < exit_end[1] and (r, c + 1) not in block_42:
            moves.append('E')

        if not moves:
            if r < height - 1:
                moves.append('S')
            if c < width - 1:
                moves.append('E')

        chosen = random.choice(moves)
        r, c = break_wall(maze, r, c, chosen)

    # Fill remaining cells
    for r in range(height):
        for c in range(width):

            if (r, c) in block_42 or (r, c) in (entry, exit_end):
                continue

            possible = []

            if r > 0 and (r - 1, c) not in block_42:
                possible.append('N')

            if c < width - 1 and (r, c + 1) not in block_42:
                possible.append('E')

            if possible:
                chosen = random.choice(possible)
                break_wall(maze, r, c, chosen)


# ==========================================================
# MAKE MAZE NON-PERFECT (Add Extra Openings)
# ==========================================================
def non_perfect(maze, width, height, block_42):

    extra_break = (width * height) // 3

    for _ in range(extra_break):

        r = random.randint(0, height - 1)
        c = random.randint(0, width - 1)

        if (r, c) in block_42:
            continue

        possible = []

        for direction, (dr, dc, _, _) in DIRECTIONS.items():
            nr, nc = r + dr, c + dc

            if (0 <= nr < height and
                0 <= nc < width and
                (nr, nc) not in block_42):
                possible.append(direction)

        if possible:
            chosen = random.choice(possible)
            break_wall(maze, r, c, chosen)


# ==========================================================
# BFS – SHORTEST PATH
# ==========================================================
def find_shortest_path_bfs(maze, start, end, width, height, block_42):

    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:
        current = queue.popleft()

        if current == end:
            break

        r, c = current

        for direction, (dr, dc, wall, _) in DIRECTIONS.items():

            if getattr(maze[r][c], wall) == 0:
                nr, nc = r + dr, c + dc

                if (0 <= nr < height and
                    0 <= nc < width and
                    (nr, nc) not in visited and
                    (nr, nc) not in block_42):

                    visited.add((nr, nc))
                    parent[(nr, nc)] = current
                    queue.append((nr, nc))

    if start != end and end not in parent:
        return [], []

    # Reconstruct path
    path = []
    node = end

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()

    # Convert to directions
    directions = []
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]

        for d, (dr, dc, _, _) in DIRECTIONS.items():
            if (r1 + dr, c1 + dc) == (r2, c2):
                directions.append(d)
                break

    return path, directions
