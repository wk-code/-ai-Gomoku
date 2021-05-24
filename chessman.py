import pygame
from pygame.sprite import Sprite


class ChessMan(Sprite):
    def __init__(self, chess_type, left, top, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.type = chess_type
        self.image = self.settings.white_img
        if self.type:
            self.image = self.settings.black_img
        self.rect = self.image.get_rect()
        self.size = self.settings.board_width // 15 // 2
        self.rect.x = left
        self.rect.y = top

    def draw(self):
        self.screen.blit(self.image, self.rect)




