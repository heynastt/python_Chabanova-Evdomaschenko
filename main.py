import pygame
from settings import *
#from game_state import *
from objects.plblock import Plblock
from objects.platform import Platform
from objects.ball import Ball
from objects.button import Button

def main():
    set_game_state_menu()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return

        SCREEN.fill((0, 0, 0))

        if GAME_STATE == "MENU":
            draw_menu()
        elif GAME_STATE == "GAME":
            run_game()
        elif GAME_STATE == "GAME_OVER":
            draw_game_over()

        pygame.display.flip()
        CLOCK.tick(60)

if __name__ == "__main__":
    main()
