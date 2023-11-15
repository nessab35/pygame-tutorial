from gameobject import GameObject
from random import randint, choice
from constants import lanes

# Cloud1
class Bird(GameObject):
    '''Bird Image'''
    def __init__(self):
        self.y = randint(50, 400)
        super().__init__(self.y, 0, 'images/bird.png')
        self.dy = 0
        self.dx = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check y position of cloud 1
        if self.x > 500 or self.y > 500 or self.x < -64 or self.y < -64:
            self.reset()

    def reset(self):
        self.y = choice(lanes)
        if randint(0, 1) == 0:
            self.x = -64
            self.dx = randint(0, 200) / 100
        else:
            self.x = 500
            self.dx = randint(0, 200) / 100
