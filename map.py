import random


class Map:
    def __init__(self, row_count, column_count):
        self.row_count = row_count
        self.column_count = column_count
        self.map = [[] * column_count] * row_count

    def get_map(self):
        return self.map

    # если значение ячейки равно :
    # - - ничего
    # s - то в ней  находится часть змеи
    # f - в ней находится еда
    # w - в ней находится часть стены

    def create_wall_on_map(self, wall):
        x, y = random.randint(1, self.map.width - 1), \
               random.randint(1, self.map.height - 1)
        if not self.can_place(x, y, wall):
            return
        if wall.orientation == 'down':
            for i in range(y, y + wall.size):
                self.map.map[x, i] = 'w'
                wall.coord.append(x, i)
        if wall.orientation == 'right':
            for i in range(x, x + wall.size):
                self.map.map[i, y] = 'w'
                wall.coord.append(i, y)

    def can_place(self, x, y, wall):
        if wall.orientation == 'down':
            if y > 0 and y + wall.size < self.row_count:
                for i in range(y, y + wall.size):
                    if self.map.map[x - 1, i] == 'w' and \
                            self.map.map[x + 1, i] == 'w':
                        return False

        if wall.orientation == 'right':
            if x > 0 and x + wall.size < self.column_count:
                for i in range(x, x + wall.size):
                    if self.map.map[i, y - 1] == 'w' and \
                            self.map.map[i, y + 1] == 'w':
                        return False
        return True

    def place_food(self, food):
