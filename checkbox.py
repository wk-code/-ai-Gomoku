import pygame


class CheckBox:
    def __init__(self, screen):
        self.box_image = pygame.image.load("")
        self.screen = screen

        self.width, self.height = 150, 50
        self.button_color = (0, 255, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('simsunnsimsun', 36)

        self.msg_image1 = self.font.render("先手", True, self.text_color, self.button_color)
        self.msg_image_rect1 = self.msg_image1.get_rect()
        self.msg_image_rect1.x = 600
        self.msg_image_rect1.y = 200

        self.msg_image2 = self.font.render("后手", True, self.text_color, self.button_color)
        self.msg_image_rect2 = self.msg_image2.get_rect()
        self.msg_image_rect2.x = 600
        self.msg_image_rect2.y = 150

        self.rect = self.msg_image_rect1

    def draw(self):
        # self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image1, self.msg_image_rect1)