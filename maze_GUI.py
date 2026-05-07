import tkinter as tk

ROWS = 15
COLS = 15
CELL_SIZE = 35

root = tk.Tk()
root.title("Maze Generator and Solver")

canvas = tk.Canvas(
    root,
    width=COLS * CELL_SIZE + 2,
    height=ROWS * CELL_SIZE + 2,
    bg="white"
)

canvas.pack()

# EMPTY STRUCTURES (NO LOGIC YET)
northWall = [[1 for _ in range(COLS)] for _ in range(ROWS + 1)]
eastWall = [[1 for _ in range(COLS + 1)] for _ in range(ROWS)]

root.mainloop()

# DRAW THE MAZE BASED ON THE WALL STRUCTURES
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


draw_maze()

# Wall remover

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


# VALIDITY CHECKER FOR A CELL

def valid(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS
