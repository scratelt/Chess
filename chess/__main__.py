"""Module containing the Chess application package."""

import tkinter as tk

BOARD_LENGTH = 800
GRID_SIZE = 8


class Square:
    square_length = BOARD_LENGTH / GRID_SIZE
    files = "ABCDEFGH"
    ranks = "87654321"

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

    def __str__(self) -> str:
        return self.position

    def __repr__(self) -> str:
        return f"Square({self.row}, {self.col}, {self.color})"

    @property
    def position(self):
        return f"{self.files[self.col]}{self.ranks[self.row]}"


class Board(tk.Canvas):
    def __init__(self, master, width: int, height: int):
        self.master = master
        self.width = width
        self.height = height

        super().__init__(master, width=width, height=height)

        self.squares = self._init_squares()
        self.bind("<Button-1>", self.left_click)

    def draw(self):
        self.draw_squares()

    def find_square(self, row: int, col: int) -> Square:
        for square in self.squares:
            if row == square.row and col == square.col:
                return square

    def draw_squares(self):
        for square in self.squares:
            square.draw(self)

    def left_click(self, event):
        print(f"event x: {event.x}, event y: {event.y}")
        col = int(event.x // Square.square_length)
        row = int(event.y // Square.square_length)
        square = self.find_square(row, col)

        old_color = square.color
        square.color = "yellow"
        self.draw()
        square.color = old_color

    @staticmethod
    def _init_squares():
        squares = []
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                square = Square(col, row)
                squares.append(square)

        return squares


def main() -> None:
    """Main entry point for the application"""
    total_squares = GRID_SIZE**2
    square_length = BOARD_LENGTH / GRID_SIZE

    # x and y sizes will be the same and board_length /grid size

    window = tk.Tk()
    window.title("Chess")
    window.geometry(f"{BOARD_LENGTH}x{BOARD_LENGTH}")

    # canvas = tk.Canvas(window, width=BOARD_LENGTH, height=BOARD_LENGTH)
    board = Board(window, width=BOARD_LENGTH, height=BOARD_LENGTH)

    board.draw()
    board.pack()

    # stuff that goes in window

    window.mainloop()


if __name__ == "__main__":
    main()
