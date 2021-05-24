import pygame
from settings import Settings
import game_function as gf
from chessboard import ChessBoard
from pygame.sprite import Group
from button import Button
from ai1 import AI


def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('五子棋')
    pygame.display.set_icon(settings.img)
    screen.fill(settings.bg_color)
    board = ChessBoard(settings, screen)
    black_chess = Group()
    white_chess = Group()
    map_list = list(list())
    button = Button(settings, screen, "开始")
    ai = AI(settings)

    for i in range(settings.line_num):
        map_list.append(list())
        for j in range(settings.line_num):
            map_list[i].append(0)

    while True:
        gf.check_event(settings, screen, black_chess, white_chess, map_list, button, ai)
        gf.update_screen(board, screen, black_chess, white_chess, button, settings)
        if settings.stat and (settings.turn and settings.player_turn == 2) or (not settings.turn and settings.player_turn == 1):
            gf.ai_play(ai, settings, map_list, black_chess, white_chess, screen, board, button)


if __name__ == '__main__':
    main()
