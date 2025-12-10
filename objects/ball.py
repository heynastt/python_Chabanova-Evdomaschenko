import pygame
from random import randint
from settings import SCREEN, SCREEN_W, SCREEN_H

class Ball:
    def __init__(self, plblock, platforms, game):
        self.plblock = plblock
        self.platforms = platforms
        self.game = game

        self.radius = 10
        self.rect = pygame.Rect(
            SCREEN_W // 2 - self.radius // 2,
            SCREEN_H - self.radius - plblock.plblock_h - 60,
            self.radius,
            self.radius
        )

        self.speed = 8
        self.dir = pygame.Vector2(randint(-100, 100), randint(-125, -75)).normalize() * self.speed
        self.image = pygame.image.load("assets/ball.png")

        self.plblock_bounce_sound = pygame.mixer.Sound("assets/bounce_plblock.mp3")
        self.break_block_sound = pygame.mixer.Sound("assets/break_block.mp3")
