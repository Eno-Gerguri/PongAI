import pygame
import math
import random


class Ball:

    def __init__(self, x, y, radius, color, max_vel):
        self.x = self.original_x = x
        self.y = self.original_y = y

        self.radius = radius
        self.color = color
        self.max_vel = max_vel

        angle = self._get_random_angle(-30, 30, [0])
        pos = 1 if random.random() < 0.5 else -1

        self._apply_random_angle(angle)
        self.x_vel *= pos

    def _get_random_angle(self, min_angle, max_angle, excluded):
        angle = 0
        while angle in excluded:
            angle = math.radians(random.randrange(min_angle, max_angle))

        return angle

    def _apply_random_angle(self, angle):
        self.x_vel = abs(math.cos(angle) * self.max_vel)
        self.y_vel = math.sin(angle) * self.max_vel

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

        angle = self._get_random_angle(-30, 30, [0])
        self._apply_random_angle(angle)

        pos = 1 if random.random() < 0.5 else -1
        self.x_vel *= pos
