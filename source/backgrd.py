import pygame
import sys
from pathlib import Path

class Background:
    def __init__(self, pathbgr, bgrwhite, pathbutton, screen) -> None:
        self.pathbgr = pathbgr
        self.bgrwhite = bgrwhite
        self.pathbutton = pathbutton
        self.screen = screen

    def background(self):
        background_image = pygame.image.load(self.pathbgr)
        self.screen.blit(background_image, (0, 0))
    def white_screen(self):
        background_image = pygame.image.load(self.bgrwhite)
        self.screen.blit(background_image, (200, 30))
    def button(self):
        path = Path(self.pathbutton)
        files = [f for f in path.rglob('*') if f.is_file()]
        for i, images in enumerate(files):
            if i < 6:
                self.screen.blit(pygame.image.load(images), (i * 150+100, 200))
            elif i < 12:
                self.screen.blit(pygame.image.load(images), ((i - 6) * 150+100, 300))
            elif i < 18:
                self.screen.blit(pygame.image.load(images), ((i - 12) * 150+100, 400))
            elif i < 24:
                self.screen.blit(pygame.image.load(images), ((i - 18) * 150+100, 500))
            else:
                self.screen.blit(pygame.image.load(images), ((i - 24) * 150+100, 600))
