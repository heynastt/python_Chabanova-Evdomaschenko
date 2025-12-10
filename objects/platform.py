import pygame
from settings import SCREEN

class Platform:
    def __init__(self, x, y):
        self.platform_w = 60
        self.platform_h = 20

        self.rect = pygame.Rect(x, y, self.platform_w, self.platform_h)
        self.image = pygame.image.load("assets/platform.png")

        self.vec_topright = pygame.Vector2(self.rect.topright) - pygame.Vector2(self.rect.center)
        self.vec_bottomright = pygame.Vector2(self.rect.bottomright) - pygame.Vector2(self.rect.center)
        self.vec_bottomleft = pygame.Vector2(self.rect.bottomleft) - pygame.Vector2(self.rect.center)
        self.vec_topleft = pygame.Vector2(self.rect.topleft) - pygame.Vector2(self.rect.center)

    def render(self):
        SCREEN.blit(self.image, self.rect)
