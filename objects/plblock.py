import pygame
from settings import SCREEN, SCREEN_W, SCREEN_H

class Plblock:
    def __init__(self):
        self.plblock_w = 100
        self.plblock_h = 15
        self.rect = pygame.Rect(
            SCREEN_W // 2 - self.plblock_w // 2,
            SCREEN_H - self.plblock_h - 60,
            self.plblock_w,
            self.plblock_h
        )
        self.plblock_speed = 6
        self.image = pygame.image.load("assets/plblock.png")

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.plblock_speed
        if key[pygame.K_RIGHT] and self.rect.x < SCREEN_W - self.plblock_w:
            self.rect.x += self.plblock_speed

    def render(self):
        self.update()
        SCREEN.blit(self.image, self.rect)
