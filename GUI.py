import tkinter as tk
import numpy as np

import life


class GUI:
    def __init__(self, seed, time_delay_ms=500, cell_size=10, canvas_size=800):
        self.root = tk.Tk()
        self.grid = life.start_game(seed, canvas_size // cell_size, canvas_size // cell_size)
        self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size)
        self.root.after(0, self.redraw, time_delay_ms, cell_size, canvas_size)
        self.root.mainloop()


    def redraw(self, time_delay_ms, cell_size, canvas_size):
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size)
        x, y = 0, 0
        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                if self.grid[row, col]:
                    self.canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill='black')
                else:
                    self.canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill='white')
                x += cell_size
            x = 0
            y += cell_size
        self.grid = life.step(self.grid)
        self.canvas.pack()
        self.root.after(time_delay_ms, self.redraw, time_delay_ms, cell_size, canvas_size)


def play():
    seed = np.array([[0, 1, 1, 1],
                     [1, 1, 1, 0]])

    random_seed = np.random.choice(a=[False, True], size=(20, 20), p=[0.5, 0.5])
    GUI(random_seed)


if __name__ == '__main__':
    play()
