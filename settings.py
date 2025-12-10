import pygame
import os

pygame.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCREEN_W = 600
SCREEN_H = 600
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))

pygame.display.set_caption('Arcanoid')
CLOCK = pygame.time.Clock()

FONT_DIR = os.path.join(BASE_DIR, "assets", "font")

TITLE_FONT = pygame.font.Font(os.path.join(FONT_DIR, "BadeenDisplay-Regular.ttf"), 70)
BUTTON_FONT = pygame.font.Font(os.path.join(FONT_DIR, "Jersey10-Regular.ttf"), 60)
SCOREBOARD_FONT = pygame.font.Font(os.path.join(FONT_DIR, "Jersey10-Regular.ttf"), 20)
GAME_OVER_FONT = pygame.font.Font(os.path.join(FONT_DIR, "Jersey10-Regular.ttf"), 60)
