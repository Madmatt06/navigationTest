import pygame
from time import sleep
from pygame.locals import K_UP,K_DOWN,K_LEFT,K_RIGHT,K_ESCAPE,KEYDOWN,KEYUP,QUIT,MOUSEBUTTONUP,MOUSEBUTTONDOWN,MOUSEMOTION
# Settings
# Screen Size
SCREEN_W, SCREEN_H = 600, 600
# Main/Forground color
MAIN_COLOR = 0xffffff
# Accent Color
ACCENT_COLOR = 0xf0aa04
# Button Color
BUTTON_COLOR = 0xc0c0c0
# Self Calculated settings
BACKGROUND_COLOR = ~MAIN_COLOR
BUTTON_CLICK_COLOR = (BUTTON_COLOR & 0xfefefe) >> 1
def main():
    running = True
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_W,SCREEN_H])
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()
    maze = []
    font = pygame.font.SysFont(None, 24)
    loading_img = font.render("Loading...", True, MAIN_COLOR << 8) # font.render seems to take rrggbbaa. This requires shifting everything over two in hex to get the right color (eight in binary)
    screen.blit(loading_img, (SCREEN_W/2-30, SCREEN_H/2-5))
    button_background = font.render("TestBackgroundButton", True, BUTTON_COLOR << 8)
    button_click = font.render("TestClickButton", True, BUTTON_CLICK_COLOR << 8)
    screen.blit(button_background, (0,0))
    screen.blit(button_click, (0,100))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Code for algorithm and UI
    pygame.quit()
