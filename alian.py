from gameobject import GameObject
from random import randint, choice
from constants import lanes

# Alian1
class Alian1(GameObject):
    '''Alian Image'''
    def __init__(self):
        self.y = randint(50, 400)
        super().__init__(self.y, 0, 'images/alian1.png')
        self.dy = 0
        self.dx = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check y position of alien1
        if self.x > 500 or self.y > 500 or self.x < -64 or self.y < -64:
            self.reset()

    def reset(self):
        reset_conditions = randint(0, 4)

        if reset_conditions == 0:
            self.x = -64
            self.y = choice(lanes)
            self.dx = (randint(0, 200) / 100) + 1
            self.dy = 0
        elif reset_conditions == 1:
            self.x = 500
            self.y = choice(lanes)
            self.dx = ((randint(0, 200) / 100) + 1) * -1
            self.dy = 0
        elif reset_conditions == 2:
            self.x = choice(lanes)
            self.y = -64
            self.dx = 0
            self.dy = (randint(0, 200) / 100) + 1
        else:
            self.x = choice(lanes)
            self.y = 500
            self.dx = 0
            self.dy = ((randint(0, 200) / 100) + 1) * -1

# Alian 2
class Alian2(GameObject):
    '''Alian 2 Image'''
    def __init__(self):
        self.y = randint(50, 400)
        super().__init__(self.y, 0, 'images/alian2.png')
        self.dy = 0
        self.dx = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check y position of bomb
        if self.x > 500 or self.y > 500 or self.x < -64 or self.y < -64:
            self.reset()

    def reset(self):
        reset_conditions = randint(0, 4)

        if reset_conditions == 0:
            self.x = -64
            self.y = choice(lanes)
            self.dx = (randint(0, 200) / 100) + 1
            self.dy = 0
        elif reset_conditions == 1:
            self.x = 500
            self.y = choice(lanes)
            self.dx = ((randint(0, 200) / 100) + 1) * -1
            self.dy = 0
        elif reset_conditions == 2:
            self.x = choice(lanes)
            self.y = -64
            self.dx = 0
            self.dy = (randint(0, 200) / 100) + 1
        else:
            self.x = choice(lanes)
            self.y = 500
            self.dx = 0
            self.dy = ((randint(0, 200) / 100) + 1) * -1
