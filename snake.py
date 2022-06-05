class Snake:
    def __init__(self):
        self.snake_length = 2
        self.cells = [(1, 0), (0, 0)]
        self.direction = 'right'
        self.baf = 'default'

    def get_cells(self):
        return self.cells
