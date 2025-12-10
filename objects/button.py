import pygame
from settings import SCREEN, BUTTON_FONT

class Button:
    def __init__(self, x, y, text, callback):
        self.rect = pygame.Rect(0, 0, 300, 100)
        self.rect.center = (x, y)
        self.text = text
        self.callback = callback
        self.pressed = False

    def update(self):
        cursor = pygame.mouse.get_pos()
        if self.rect.collidepoint(cursor):
            if any(pygame.mouse.get_pressed()):
                self.pressed = True
            elif self.pressed:
                self.callback()
                self.__init__(self.rect.centerx, self.rect.centery, self.text, self.callback)
        else:
            self.pressed = False

    def render(self):
        self.update()
        t = BUTTON_FONT.render(self.text, True, (255,255,255))
        pygame.draw.rect(SCREEN, (139,0,0) if self.pressed else (90,0,0), self.rect)
        SCREEN.blit(t, t.get_rect(center=self.rect.center))
