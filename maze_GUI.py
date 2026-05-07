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