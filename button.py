import pygame.font


class Button:

    def __init__(self, setting, screen, msg):
        self.screen = screen
        # self.screen_rect = screen.get_rect()

        self.width, self.height = 50, 25  # 36 : (74, 38)
        self.button_color = (215, 215, 215)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('simsunnsimsun', 24)
        self.msg = msg
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

        # self.rect = pygame.Rect(0, 0, self.width, self.height)
        # self.rect.center = self.screen_rect.center

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.x = 625
        self.msg_image_rect.y = 380

        self.frame = pygame.Rect(self.msg_image_rect.x - 2, self.msg_image_rect.y - 2, self.width + 2, self.height + 2)
        self.frame_color = (30, 144, 235)
        self.frame_width = 3

        self.rect = self.msg_image_rect

    def draw_button(self):
        # self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        pygame.draw.rect(self.screen, self.frame_color, self.frame, width=self.frame_width)

    def change_text(self, msg):
        self.msg = msg
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

    def change_color(self, button_type):
        if button_type:
            self.frame_width = 2
            self.button_color = (230, 230, 230)
            self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        else:
            self.frame_width = 3
            self.button_color = (215, 215, 215)
            self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
