class Logic:
    def __init__(self, snake, wall_list, food, column_count, row_count, speed,
                 direction):
        self.snake = snake
        self.wall_list = wall_list
        self.food = food
        self.column_count = column_count
        self.row_count = row_count
        self.speed = speed
        self.direction = direction

    def check_collision(self):
        return True if self.snake.cells[0] in self.snake.cells()[1:] else False

    def move(self, direction):
        x, y = self.snake.cells[0]

        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'right':
            x += 1
        elif direction == 'left':
            x -= 1
        self.snake.cells.insert(0, (x, y))
        del self.snake.cells[-1]

    def food_was_eat_or_not(self):
        if self.snake.cells[0] == self.food.cell:
            self.snake.cells.insert(0, self.food.cell)
            if self.food.baf == 'double_up':
                x, y = self.snake.cells[-1]
                if self.direction == 'down':
                    self.snake.cells.insert(-1, (x, y - 1))
                if self.direction == 'up':
                    self.snake.cells.insert(-1, (x, y + 1))
                if self.direction == 'right':
                    x, y = self.snake.cells[-1]
                    self.snake.cells.insert(-1, (x - 1, y))
                if self.direction == 'left':
                    x, y = self.snake.cells[-1]
                    self.snake.cells.insert(-1, (x + 1, y))
                self.snake.baf = 'default'
            if self.food.baf == 'low_speed':
                self.speed += 5

    def exit_border(self):
        x, y = self.snake.cells[0]
        if x < 0 or x > self.column_count - 1:
            if x < 0:
                x = self.column_count - 1
            else:
                x = 0
        if y < 0 or y > self.row_count - 1:
            if y < 0:
                y = self.row_count - 1
            else:
                y = 0
        return x, y

    def collision_with_wall(self):
        if self.snake.baf == 'shield' and \
                (self.snake.cells[0] == (x, y) for x, y in self.wall_list):
            self.snake.baf = 'default'
            return False
        if (self.snake.cells[0] == (x, y) for x, y in self.wall_list):
            return True
        else:
            return False

    def change_direction(self, new_direction):
        direction = self.direction
        if new_direction == 'down':
            if direction != 'up':
                direction = new_direction
        if new_direction == 'up':
            if direction != 'down':
                direction = new_direction
        if new_direction == 'right':
            if direction != 'left':
                direction = new_direction
        if new_direction == 'left':
            if direction != 'right':
                direction = new_direction
        return direction
