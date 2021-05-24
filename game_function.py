import pygame
import sys
from chessman import ChessMan
from node import Node


def update_screen(board, screen, black_chess, white_chess, button, settings):
    screen.fill(settings.bg_color)
    board.draw_board()
    black_chess.draw(screen)
    white_chess.draw(screen)
    button.draw_button()
    pygame.display.flip()


def check_event(settings, screen, black_chess, white_chess, map_list, button, ai):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if settings.stat:
                if (settings.line_initial_left + settings.width * (settings.line_num - 1) + settings.width // 2 >
                        mouse_x > settings.line_initial_left - settings.width // 2
                        and settings.line_initial_top + settings.width * (settings.line_num - 1) + settings.width // 2 >
                        mouse_y > settings.line_initial_top - settings.width // 2):
                    update_board(mouse_x, mouse_y, settings, screen, black_chess, white_chess, map_list, button, ai)
            check_click_button(mouse_x, mouse_y, button, settings, black_chess, white_chess, map_list)
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button.rect.collidepoint(mouse_x, mouse_y):
                button.change_color(True)
            else:
                button.change_color(False)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button.change_color(False)


def check_click_button(mouse_x, mouse_y, button, settings, black_chess, white_chess, map_list):
    if button.rect.collidepoint(mouse_x, mouse_y):
        button.change_color(True)
        if settings.stat:
            settings.stat = False
            button.change_text("开始")
            settings.max_x = -1
            settings.min_x = 15
            settings.max_y = -1
            settings.min_y = 15

        else:
            settings.stat = True
            button.change_text("结束")
            black_chess.empty()
            white_chess.empty()
            settings.turn = True
            for i in range(settings.line_num):
                for j in range(settings.line_num):
                    map_list[i][j] = 0


def update_board(x, y, settings, screen, black_chess, white_chess, map_list, button, ai):
    (left, top) = check_mouse(x, y, settings, map_list, button)
    if left < 0:
        return
    chess = ChessMan(settings.turn, left, top, settings, screen)
    if settings.turn:
        black_chess.add(chess)
    else:
        white_chess.add(chess)
    settings.setTurn()

    # print(score.x, score.y)
    # print(score.grade)


def ai_play(ai, settings, map_list, black_chess, white_chess, screen, board, button):
    score = ai.get_result(map_list, black_chess)
    ai_left = score.x * settings.width + settings.line_initial_left - settings.width // 2 + 1
    ai_top = score.y * settings.width + settings.line_initial_top - settings.width // 2 + 1
    print(score.x, " ", score.y)
    chess_ai = ChessMan(settings.turn, ai_left, ai_top, settings, screen)
    map_list[score.x][score.y] = ai.turn
    if ai.turn == 1:
        black_chess.add(chess_ai)
    else:
        white_chess.add(chess_ai)
    settings.setTurn()
    update_screen(board, screen, black_chess, white_chess, button, settings)
    settings.winner = check_win(map_list, score.x, score.y, settings, button)


def check_mouse(x, y, settings, map_list, button):
    xt = int((x - settings.line_initial_left + settings.width // 2) // settings.width)
    yt = int((y - settings.line_initial_top + settings.width // 2) // settings.width)
    left = xt * settings.width + settings.line_initial_left - settings.width // 2 + 1
    top = yt * settings.width + settings.line_initial_top - settings.width // 2 + 1

    if map_list[xt][yt] != 0:
        return -1, -1

    if settings.turn:
        map_list[xt][yt] = 1
    else:
        map_list[xt][yt] = 2

    if xt > settings.max_x:
        settings.max_x = xt
    if xt < settings.min_x:
        settings.min_x = xt
    if yt > settings.max_y:
        settings.max_y = yt
    if yt < settings.min_y:
        settings.min_y = yt

    settings.winner = check_win(map_list, xt, yt, settings, button)

    return left, top


def check_win(map_list, x, y, settings, button):
    # 检查8个方向
    # 0 1 2
    # 3   4
    # 5 6 7
    if check_chess(map_list, x, y, -1, -1) + check_chess(map_list, x, y, 1, 1) > 3 or \
            check_chess(map_list, x, y, 0, -1) + check_chess(map_list, x, y, 0, 1) > 3 or \
            check_chess(map_list, x, y, 1, -1) + check_chess(map_list, x, y, -1, 1) > 3 or \
            check_chess(map_list, x, y, -1, 0) + check_chess(map_list, x, y, 1, 0) > 3:
        settings.stat = False
        button.change_text("开始")
        temp = map_list[x][y]
        for i in range(settings.line_num):
            for j in range(settings.line_num):
                map_list[i][j] = 0
        return temp
    else:
        return 0


def check_chess(map_list, x, y, x_change, y_change):
    chess_type = map_list[x][y]
    n = 0
    for i in range(4):
        x += x_change
        y += y_change
        if x < 0 or y < 0 or x > 14 or y > 14:
            return n
        if map_list[x][y] != chess_type:
            return n
        n += 1
    return n
