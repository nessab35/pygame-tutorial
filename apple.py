from gameobject import GameObject
from random import randint, choice
from constants import lanes, fruit_captured


# Apple
class Apple(GameObject):
    '''Class for apple image'''
    def __init__(self):
        x = randint(50, 400)
        super().__init__(x, 0, 'images/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check the y position of the apple
        if self.x > 500 or self.y > 500 or self.x < -64 or self.y < -64:
            self.reset()

    def reset(self):
        self.x = choice(lanes)
        if randint(0, 1) == 0:
            self.y = -64
            self.dy = (randint(0, 200) / 100) + fruit_captured
        else:
            self.y = 500
            self.dy = (-((randint(0, 200) / 100) + fruit_captured))
