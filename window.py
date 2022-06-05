from logic import *
from tkinter import *


class Window:
    def __init__(self, width, height, back_ground_color, space_size):
        # 1000, 600, 'black', 25;
        self.Tk = Tk()
        self.width = width
        self.height = height
        self.back_ground_color = back_ground_color
        self.space_size = space_size
        self.canvas = Canvas(self.Tk, height=height, width=width,
                             bg=back_ground_color)
        self.Tk.mainloop()..
        self.Tk.resizable(False, False)
        self.Tk.title('Змейка')
        self.Tk.geometry(f'{self.width}x{self.height}')


    def clean_map(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(self.canvas.winfo_width() / 2,
                                self.canvas.winfo_height() / 2,
                                font=('Future PT', 50), text='Game Over',
                                fill='orange')

    def bind_control(self):
        self.Tk.bind('<Up>', lambda event: change_direction('up'))
        self.Tk.bind('<Down>', lambda event: change_direction('down'))
        self.Tk.bind('<Right>', lambda event: change_direction('right'))
        self.Tk.bind('<Left>', lambda event: change_direction('left'))
