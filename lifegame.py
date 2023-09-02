import config
import random

class LifeGame:
    def __init__(self):
        self._field = []
        self._iteration = 0
        self.initField()

    def initField(self):
        self._field = []
        for _ in range(config.WIDTH):
            line = []
            for _ in range(config.HEIGHT):
                line.append(config.EMPTY)
            self._field.append(line)

    def shuffle(self):
        shuffled = []
        for line in self._field:
            new_line = []
            for _ in line:
                new_sell = random.choice([config.EMPTY, config.LIFE])
                new_line.append(new_sell)
            shuffled.append(new_line)
        self._field = shuffled

    def update(self):
        self._iteration += 1
        updated = []
        for row, line in enumerate(self._field):
            new_line = []
            for col, sell in enumerate(line):
                sell = self.judge(row, col)
                new_line.append(sell)
            updated.append(new_line)
        self._field = updated

    def judge(self, row, col):
        cnt = 0
        x_min = max(col - 1, 0)
        x_max = min(col + 2, config.WIDTH)
        y_min = max(row - 1, 0)
        y_max = min(row + 2, config.HEIGHT)
        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                sell = self._field[y][x]
                if sell == config.LIFE:
                    cnt += 1
        sell = self._field[row][col]
        if sell == config.LIFE:
            cnt -= 1
            if cnt <= config.SPARSE:
                return config.EMPTY
            elif cnt >= config.DENSE:
                return config.EMPTY
            return config.LIFE
        else:
            if cnt == config.BIRTH:
                return config.LIFE
            return config.EMPTY

    def print(self):
        print(f"Iteration: {str(self._iteration)}")
        d = "+" + "-" * (config.WIDTH * 2 - 1) + "+"
        print(d)
        for line in self._field:
            l = "|"
            for col in line:
                if col == config.LIFE:
                    l += "*|"
                else:
                    l += " |"
            print(l)
        print(d)

          
    
