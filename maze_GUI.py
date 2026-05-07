import tkinter as tk
import random
import time

# SETTINGS
DELAY = 0.03
ROWS = 15
COLS = 15
CELL_SIZE = 35

# WINDOW
root = tk.Tk()
root.title("Maze Generator and Solver")

canvas = tk.Canvas(
    root,
    width=COLS * CELL_SIZE + 2,
    height=ROWS * CELL_SIZE + 2,
    bg="white"
)
canvas.pack()

# DATA STRUCTURES
northWall = [[1 for _ in range(COLS)] for _ in range(ROWS + 1)]
eastWall = [[1 for _ in range(COLS + 1)] for _ in range(ROWS)]
visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
solverVisited = [[False for _ in range(COLS)] for _ in range(ROWS)]


# VALID CELL
def valid(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS


# REMOVE WALL
def remove_wall(current, nxt):
    r1, c1 = current
    r2, c2 = nxt

    dr = r2 - r1
    dc = c2 - c1

    if dr == -1:
        northWall[r1][c1] = 0
    elif dr == 1:
        northWall[r2][c2] = 0
    elif dc == 1:
        eastWall[r1][c1 + 1] = 0
    elif dc == -1:
        eastWall[r1][c1] = 0


# DRAW MAZE
def draw_maze():

    canvas.delete("all")

    for r in range(ROWS):
        for c in range(COLS):

            x1 = c * CELL_SIZE
            y1 = r * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            if northWall[r][c]:
                canvas.create_line(x1, y1, x2, y1, width=2)

            if eastWall[r][c + 1]:
                canvas.create_line(x2, y1, x2, y2, width=2)

            if c == 0:
                canvas.create_line(x1, y1, x1, y2, width=2)

            if r == ROWS - 1:
                canvas.create_line(x1, y2, x2, y2, width=2)

    root.update()


# DFS MAZE GENERATION
def generate_maze():

    stack = []
    start = (0, 0)

    stack.append(start)
    visited[0][0] = True

    while stack:

        current = stack[-1]
        r, c = current

        neighbors = []
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for dr, dc in directions:

            nr, nc = r + dr, c + dc

            if valid(nr, nc) and not visited[nr][nc]:
                neighbors.append((nr, nc))

        if neighbors:

            nxt = random.choice(neighbors)

            remove_wall(current, nxt)

            # BONUS FEATURE
            # RANDOM EXTRA WALL REMOVAL
            # Creates cycles / loops
          
            if random.randint(1, 20) == 1:

                extra_dirs = [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1)
                ]

                random.shuffle(extra_dirs)

                for dr, dc in extra_dirs:

                    er = current[0] + dr
                    ec = current[1] + dc

                    if valid(er, ec):

                        remove_wall(current, (er, ec))
                        break

            nr, nc = nxt
            visited[nr][nc] = True
            stack.append(nxt)

            draw_maze()
            time.sleep(DELAY)

        else:
            stack.pop()

  
  # CHECK MOVEMENT
def can_move(r1, c1, r2, c2):

    if not valid(r2, c2):
        return False

    dr = r2 - r1
    dc = c2 - c1

    if dr == -1:
        return northWall[r1][c1] == 0
    elif dr == 1:
        return northWall[r2][c2] == 0
    elif dc == 1:
        return eastWall[r1][c1 + 1] == 0
    elif dc == -1:
        return eastWall[r1][c1] == 0

    return False

# COLOR CELL
def color_cell(r, c, color):

    padding = 6

    x1 = c * CELL_SIZE + padding
    y1 = r * CELL_SIZE + padding

    x2 = x1 + CELL_SIZE - 2 * padding
    y2 = y1 + CELL_SIZE - 2 * padding

    canvas.create_oval(
        x1,
        y1,
        x2,
        y2,
        fill=color,
        outline=color
    )

    root.update()
    time.sleep(DELAY)


# SOLVE MAZE
# BACKTRACKING

def solve_maze(r, c, end_r, end_c):

    solverVisited[r][c] = True

    # current mouse
    color_cell(r, c, "red")

    if r == end_r and c == end_c:

        # correct path
        color_cell(r, c, "green")
        return True

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    random.shuffle(directions)

    for dr, dc in directions:

        nr = r + dr
        nc = c + dc

        if (
            valid(nr, nc)
            and not solverVisited[nr][nc]
            and can_move(r, c, nr, nc)
        ):

            if solve_maze(nr, nc, end_r, end_c):

                color_cell(r, c, "green")
                return True

    # dead end
    color_cell(r, c, "blue")

    return False


# START PROGRAM
draw_maze()

generate_maze()
#intrance walls
northWall[0][0] = 0
#exit walls
northWall[ROWS][COLS - 1] = 0

draw_maze()

solve_maze(0, 0, ROWS - 1, COLS - 1)

root.mainloop()