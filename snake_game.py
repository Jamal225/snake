import random
from tkinter import *
import time


class Snake:
    def __init__(self):
        self.snake_length = 3
        self.coord = [[0, 0]] * 3
        self.squares = []

        for x, y in self.coord:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE,
                                             y + SPACE_SIZE,
                                             fill=COLOR_BODY)
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0,
                           int((WINDOW_WIDTH - SPACE_SIZE) / SPACE_SIZE - 1)) \
            * SPACE_SIZE

        y = random.randint(0,
                           int((WINDOW_HEIGHT - 2 * SPACE_SIZE) /
                               SPACE_SIZE - 1)) * SPACE_SIZE

        self.coord = [x, y]

        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                fill=FOOD_COLOR)


def check_collision(self):
    x, y = self.coord[0]
    for e in self.coord[1:]:
        if x == e[0] and y == e[1]:
            return True


def move(snakes, foods):
    for x, y in snakes.coord:
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                fill=COLOR_BODY)
    x, y = snakes.coord[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE

    snakes.coord.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                     fill=COLOR_HEAD)
    snakes.squares.insert(0, square)
    if x == foods.coord[0] and y == foods.coord[1]:
        global score
        score += 1
        label_score.config(text=f'Score: {score}')
        canvas.delete('food')
        foods = Food()
    else:
        x, y = snakes.coord[-1]
        canvas.create_rectangle(x, y, x + SPACE_SIZE,
                                y + SPACE_SIZE, fill='black')
        del snakes.coord[-1]
        canvas.delete(snakes.squares[-1])
        del snakes.squares[-1]

    x, y = snakes.coord[0]
    if x < 0 or x > WINDOW_WIDTH - SPACE_SIZE:
        if x < 0:
            x = WINDOW_WIDTH - SPACE_SIZE
        elif x > WINDOW_WIDTH - SPACE_SIZE:
            x = 0
        snakes.coord.insert(0, (x, y))
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                fill=COLOR_HEAD)
    if y < 0 or y > WINDOW_HEIGHT - 2 * SPACE_SIZE:
        if y < 0:
            y = WINDOW_HEIGHT - 2 * SPACE_SIZE
        elif y > WINDOW_HEIGHT - 2 * SPACE_SIZE:
            y = 0
        snakes.coord.insert(0, (x, y))
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                fill=COLOR_HEAD)
    if check_collision(snakes):
        game_over()
    else:
        window.after(SPEED, move, snakes, foods)
    print(snakes.coord)


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('Future PT', 50), text='Game Over', fill='orange')


def change_direction(next_direction):
    global direction
    if next_direction == 'down':
        if direction != 'up':
            direction = next_direction
    if next_direction == 'up':
        if direction != 'down':
            direction = next_direction
    if next_direction == 'right':
        if direction != 'left':
            direction = next_direction
    if next_direction == 'left':
        if direction != 'right':
            direction = next_direction
    time.sleep(0.15)


if __name__ == '__main__':
    # WINDOW_WIDTH: int = 1000
    # WINDOW_HEIGHT = 600
    # BACKGROUND_COLOR = 'black'
    # FOOD_COLOR = 'white'
    # COLOR_BODY = '#ff42d0'
    # COLOR_HEAD = '#4b0082'
    # SPACE_SIZE: int = 25
    # SPEED = 100
    # SNAKE_LEN = 3
    # direction = 'right'
    #
    # window = Tk()
    # window.title('Змейка')
    # window.resizable(False, False)
    # window.geometry('1000x600')
    #
    # score = 0
    # label_score = Label(window, text='Счет: {}'.format(score),
    #                     font={'Arial', 20})
    # label_score.pack()
    #
    # canvas = Canvas(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH,
    #                 bg=BACKGROUND_COLOR)
    # canvas.pack()
    #
    # snake = Snake()
    # food = Food()
    # move(snake, food)
    #
    # window.bind('<Up>', lambda event: change_direction('up'))
    # window.bind('<Down>', lambda event: change_direction('down'))
    # window.bind('<Right>', lambda event: change_direction('right'))
    # window.bind('<Left>', lambda event: change_direction('left'))
    #
    # window.mainloop()
    qwer = 0.0
    for i in range(1, 100000):
        qwer = (3 ** (1 / i) - 1)
        print(qwer,' ', 1/i)
