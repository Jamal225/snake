from Game import Game
from Rendering import Rendering
from window import Window

if __name__ == '__main__':
    game = Game(1000, 600)
    window = Window(1000, 600, 'black', 25)
    rander = Rendering(game, window)

    rander.draw_wall()

    window.Tk.mainloop()
