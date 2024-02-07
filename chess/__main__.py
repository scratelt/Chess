"""Module containing the Chess application package."""

import tkinter as tk


def main() -> None:
    """Main entry point for the application"""

    board_length = 800
    grid_size = 2  # 2x2 grid

    total_squares = grid_size**2
    square_length = board_length / grid_size

    # x and y sizes will be the same and board_length /grid size

    window = tk.Tk()
    window.title("Chess")
    window.geometry(f"{board_length}x{board_length}")

    canvas = tk.Canvas(window, width=board_length, height=board_length)

    # loop - increment x and y by board_length / grid_size, then keep y constant and increment x until x is board_length, then reset x to 0. increment Y again and repeat until y is board_length for last loop.

    upper_left = (0, 0)
    lower_right = (board_length, board_length)

    canvas.create_rectangle(*upper_left, *lower_right, fill="blue")

    # canvas.create_rectangle(x1, y1, x2, y2, fill="color")

    canvas.create_rectangle(0, 0, 400, 400, fill="red")
    canvas.create_rectangle(400, 0, 800, 400, fill="black")
    canvas.create_rectangle(0, 400, 400, 800, fill="red")
    canvas.create_rectangle(400, 400, 800, 800, fill="black")

    canvas.pack()

    # stuff that goes in window

    window.mainloop()


if __name__ == "__main__":
    main()
