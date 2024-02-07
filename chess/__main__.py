"""Module containing the Chess application package."""

import tkinter as tk

BOARD_LENGTH = 800
GRID_SIZE = 8


class Square:
    square_length = BOARD_LENGTH / GRID_SIZE

    def __init__(self, col, row):
        self.row = row
        self.col = col
        self.x1 = col * self.square_length
        self.y1 = row * self.square_length
        self.x2 = self.x1 + self.square_length
        self.y2 = self.y1 + self.square_length
        self.color = "red" if (self.row + self.col) % 2 == 0 else "black"

    def draw(self, canvas):
        canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2, fill=self.color
        )


def main() -> None:
    """Main entry point for the application"""
    total_squares = GRID_SIZE**2
    square_length = BOARD_LENGTH / GRID_SIZE

    # x and y sizes will be the same and board_length /grid size

    window = tk.Tk()
    window.title("Chess")
    window.geometry(f"{BOARD_LENGTH}x{BOARD_LENGTH}")

    canvas = tk.Canvas(window, width=BOARD_LENGTH, height=BOARD_LENGTH)

    # loop - increment x and y by board_length / grid_size, then keep y constant and increment x until x is board_length, then reset x to 0. increment Y again and repeat until y is board_length for last loop.

    upper_left = (0, 0)
    lower_right = (BOARD_LENGTH, BOARD_LENGTH)

    canvas.create_rectangle(*upper_left, *lower_right, fill="blue")

    # canvas.create_rectangle(x1, y1, x2, y2, fill="color")

    # canvas.create_rectangle(0, 0, 400, 400, fill="red")
    # canvas.create_rectangle(400, 0, 800, 400, fill="black")
    # canvas.create_rectangle(0, 400, 400, 800, fill="red")
    # canvas.create_rectangle(400, 400, 800, 800, fill="black")
    squares = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            square = Square(col, row)
            square.draw(canvas)
            squares.append(square)

    # row x grid_size + col
    canvas.pack()

    # stuff that goes in window

    window.mainloop()


if __name__ == "__main__":
    main()
