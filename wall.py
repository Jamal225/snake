import random


class Wall:
    def __init__(self):
        self.cells = []
        self.orientation = random.choice(['down', 'right'])
        self.size = random.randint(2, 4)

    def init_cells(self, cell):
        if self.orientation == 'down':
            for i in range(0, self.size):
                self.cells.append((cell[0], cell[1] + i))

        if self.orientation == 'right':
            for i in range(0, self.size):
                self.cells.append((cell[0] + i, cell[1]))
