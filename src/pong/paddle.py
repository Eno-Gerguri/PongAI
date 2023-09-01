import pygame


class Paddle:
    UP = 1
    DOWN = 0
    LEFT = 1
    RIGHT = 0

    def __init__(self, x, y, width, height, color, vel):
        self.x = self.original_x = x
        self.y = self.original_y = y

        self.width = width
        self.height = height
        self.color = color
        self.vel = vel

    def draw(self, win):
        pygame.draw.rect(
                win,
                self.color,
                (self.x, self.y, self.width, self.height)
        )

    def move(self, up=UP):
        if up:
            self.y -= self.vel
        else:
            self.y += self.vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
