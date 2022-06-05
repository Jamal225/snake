import random


class Food:
    def __init__(self):
        self.cell = ()

        self.baf = ['shield', 'double_up', 'low_speed', 'default', 'default',
                    'default', 'default']

    def get_cell(self):
        return self.cell

    def get_baf(self):
        return self.baf
