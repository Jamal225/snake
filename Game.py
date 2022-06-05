import random
from logic import Logic
from wall import Wall
from food import Food
from snake import Snake


class Game:
    def __init__(self, row_count, column_count):
        self.column_count = column_count  # горизонталь
        self.row_count = row_count  # вертикаль
        self.wall_list = []
        food = Food()
        self.food = food
        snake = Snake()
        self.snake = snake

    def create_wall_(self, wall):
        x, y = random.randint(1, self.column_count - 1), \
               random.randint(1, self.row_count - 1)
        if not self.can_place_wall(x, y, wall):
            return
        wall.init_cells((x, y))
        self.wall_list.append(wall)

    def can_place_wall(self, x, y, wall):
        if wall.orientation == 'down':
            if y > 0 and y + wall.size < self.row_count:
                for e in self.wall_list:
                    for cell in e.get_cells:
                        if cell == (x, y):
                            return False

        if wall.orientation == 'right':
            if x > 0 and x + wall.size < self.column_count:
                for e in self.wall_list:
                    for cell in e.get_cells:
                        if cell == (x, y):
                            return False
        return True

    def place_food(self):
        x, y = 0, 0
        cell = None
        while cell is None:
            x = random.randint(1, self.column_count)
            y = random.randint(1, self.row_count)
            if not self.can_place_food(x, y):
                cell = None
            else:
                break
        return x, y

    def can_place_food(self, x, y):
        for e in self.wall_list:
            for cell in e.cells:
                if cell == (x, y):
                    return False

        for e in self.snake.cells:
            if e == (x, y):
                return False
        return True

    def can_place_snake(self, x, y):
        if 2 < x < self.column_count:
            for e in self.wall_list:
                for cell in e.cells:
                    if cell == (x, y) and cell == (x - 1, y):
                        return False
            if (x - 1, y) == self.food.cell:
                return False
        return True

    def place_snake(self):
        self.snake.cells.clear()
        x = random.randint(1, self.column_count)
        y = random.randint(1, self.row_count)
        if not self.can_place_snake(x, y):
            return
        self.snake.cells.append((x, y))

    def game_build(self, wall_count):

        while len(self.wall_list) != wall_count:
            wall = Wall()
            self.create_wall_(wall)

        self.food.coord = self.place_food()

        while len(self.snake.cells != 2):
            self.place_snake()

    def game(self):
        self.game_build(4)

