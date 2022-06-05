from tkinter import *


class Rendering:
    def __init__(self, game, window):
        self.window = window
        self.snake = game.snake
        self.food = game.food
        self.wall = game.wall
        self.canvas = Canvas(window, height=window.height, width=window.width,
                             bg=window.back_ground_color)

    def draw_snake(self):
        squares = []
        for x, y in self.snake.get_coord()[1:]:
            square_for_body = \
                self.canvas.create_rectangle(x, y, x + self.window.space_size,
                                             y + self.window.space_size,
                                             fill='#ff42d0')
            squares.append(square_for_body)
        x, y = self.snake.get_coord()[0]
        square_for_head = \
            self.canvas.create_rectangle(x, y,
                                         x + self.window.space_size,
                                         y + self.window.space_size,
                                         fill='#4b0082')
        squares.insert(0, square_for_head)

    def draw_food(self):
        foodColor = 'white'
        x, y = self.food.getCoord
        self.canvas.create_rectangle(x, y, x + self.window.space_size,
                                     y + self.window.space_size,
                                     fill=foodColor)

    def draw_wall(self):
        for x, y in self.wall.get_coord():
            self.canvas.create_rectangle(x, y, x + self.window.space_size,
                                         y + self.window.space_size,
                                         fill='red')
