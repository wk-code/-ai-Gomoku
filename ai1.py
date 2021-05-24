import copy
from node import Node
import random

first_hand = [[1]
    , [1]
    , []
    , []]


class AI:
    def __init__(self, settings):
        self.depth = 1
        self.turn = 1
        self.settings = settings
        if settings.player_turn == 1:
            self.turn = 2

    def first_hand(self, node, black_chess):
        pass

    def get_result(self, map_list, black_chess):
        map_temp = copy.deepcopy(map_list)
        root = Node(-1, -1, 0)

        self.depth_first_traversal(root, 1, map_temp)
        return root

    def depth_first_traversal(self, node, depth, map_temp):
        if depth <= self.depth:
            self.find_child_node(map_temp, node)
        else:
            node.grade = self.cal_grade(map_temp, node.x, node.y)
            return node.grade

        turn = self.turn
        if depth % 2 == 0:
            if self.turn == 1:
                turn = 2
            else:
                turn = 1
        temp_node = []

        if len(node.child) != 0:
            for ele in node.child.copy():
                map_temp[ele.x][ele.y] = turn
                grade = self.depth_first_traversal(ele, depth + 1, map_temp)
                if grade >= node.grade:
                    if depth == 1:
                        if grade != node.grade:
                            temp_node.clear()
                        temp_node.append(ele)
                    node.grade = grade

                map_temp[ele.x][ele.y] = 0

        if depth == 1:
            # 测试计分是否正确
            list1 = list(list())
            for i in range(self.settings.line_num):
                list1.append(list())
                for j in range(self.settings.line_num):
                    list1[i].append(-1)
            for ele in node.child.copy():
                list1[ele.y][ele.x] = ele.grade
            for i in range(self.settings.line_num):
                for j in range(self.settings.line_num):
                    print("%4d" % list1[i][j], end='')
                print()
            print()
            if len(temp_node) == 0:
                node.x = 7
                node.y = 7
            else:
                index = random.randint(0, len(temp_node) - 1)
                node.x = temp_node[index].x
                node.y = temp_node[index].y

    def find_child_node(self, map_temp, node):
        effect = 3
        x_min = self.settings.min_x - effect if self.settings.min_x - effect > -1 else 0
        x_max = self.settings.max_x + effect if self.settings.max_x + effect < 15 else 14
        y_min = self.settings.min_y - effect if self.settings.min_y - effect > -1 else 0
        y_max = self.settings.max_y + effect if self.settings.max_y + effect < 15 else 14

        for i in range(x_min, x_max + 1):
            for j in range(y_min, y_max + 1):
                if map_temp[i][j] == 0:
                    new_node = Node(i, j, 0)
                    node.add_child(new_node)

    def cal_grade(self, map_list, x, y):
        # 0 1 2
        # 3   3
        # 2 1 0
        score = 0
        turn = map_list[x][y]
        ene_turn = 0
        if turn == 1:
            ene_turn = 2
        else:
            ene_turn = 1

        score = score + self.cal_line(map_list, x, y, -1, -1, turn) + self.cal_line(map_list, x, y, -1, -1,
                                                                                    ene_turn) / 4 * 2
        score = score + self.cal_line(map_list, x, y, 0, -1, turn) + self.cal_line(map_list, x, y, 0, -1,
                                                                                   ene_turn) / 4 * 2
        score = score + self.cal_line(map_list, x, y, 1, -1, turn) + self.cal_line(map_list, x, y, 1, -1,
                                                                                   ene_turn) / 4 * 2
        score = score + self.cal_line(map_list, x, y, -1, 0, turn) + self.cal_line(map_list, x, y, -1, 0,
                                                                                   ene_turn) / 4 * 2

        return score

    def cal_line(self, map_list, x, y, x_change, y_change, turn):
        pre_x = x
        pre_y = y
        if turn == 1:
            ene_turn = 2
        else:
            ene_turn = 1

        obstruct = 0  # 直接阻挡
        null_obstruct = 0  # 间接阻挡
        chess_num = 0  # 连着棋子数目
        null_chess_num = 0  # 间隔一子数目
        null_chess_num1 = 0  # 连续间隔一子数目
        null_null_chess_num = 0  # 间隔两字数目

        continuous_null = 0

        pre_pa = map_list[x][y]
        x += x_change
        y += y_change

        while (-1 < x < 15 and -1 < y < 15) and map_list[x][y] != ene_turn and continuous_null < 3:
            if map_list[x][y] == 0:
                continuous_null += 1
            else:
                if continuous_null == 1:
                    null_chess_num += 1
                elif continuous_null == 2:
                    if null_chess_num == 0:
                        null_null_chess_num += 1
                    else:
                        null_chess_num1 += 1
                    # if pre_pa == 0:
                    #     null_null_chess_num += 1
                    # else:
                    #     null_chess_num1 += 1
                elif continuous_null == 0:
                    chess_num += 1

            pre_pa = map_list[x][y]
            x += x_change
            y += y_change
            if x < 0 or x > 14 or y < 0 or y > 14:
                break

        if -1 < x < 15 and -1 < y < 15:
            if map_list[x][y] == ene_turn:
                if pre_pa == 0:
                    if continuous_null == 1:
                        null_obstruct += 1
                else:
                    obstruct += 1
        else:
            if pre_pa == 0:
                null_obstruct += 1
            else:
                obstruct += 1

        x = pre_x
        y = pre_y
        pre_pa = turn
        x_change = -x_change
        y_change = -y_change

        x += x_change
        y += y_change

        front_obstruct = obstruct
        front_chess_num = chess_num
        front_null_obstruct = null_obstruct
        front_null_chess_num = null_chess_num
        front_null_chess_num1 = null_chess_num1
        front_null_null_chess_num = null_null_chess_num

        continuous_null = 0
        obstruct = 0  # 直接阻挡
        null_obstruct = 0  # 间接阻挡
        null_chess_num = 0  # 间隔一子数目
        null_chess_num1 = 0  # 连续间隔一子数目
        null_null_chess_num = 0  # 间隔两字数目

        while (-1 < x < 15 and -1 < y < 15) and map_list[x][y] != ene_turn and continuous_null < 3:
            if map_list[x][y] == 0:
                continuous_null += 1
            else:
                if continuous_null == 1:
                    null_chess_num += 1
                elif continuous_null == 2:
                    if null_chess_num == 0:
                        null_null_chess_num += 1
                    else:
                        null_chess_num1 += 1
                    # if pre_pa == 0:
                    #     null_null_chess_num += 1
                    # else:
                    #     null_chess_num1 += 1
                elif continuous_null == 0:
                    chess_num += 1

            pre_pa = map_list[x][y]
            x += x_change
            y += y_change

        if -1 < x < 15 and -1 < y < 15:
            if map_list[x][y] == ene_turn:
                if pre_pa == 0:
                    if continuous_null == 1:
                        null_obstruct += 1
                else:
                    obstruct += 1
        else:
            if pre_pa == 0:
                null_obstruct += 1
            else:
                obstruct += 1

        all_num = chess_num + front_null_chess_num + null_chess_num + front_null_chess_num1 \
                  + null_chess_num1 + front_null_null_chess_num + null_null_chess_num

        if all_num == 0:
            return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 0, 0,
                                       null_obstruct + front_null_obstruct)

        elif all_num == 1:

            if front_null_null_chess_num == 1 or null_null_chess_num == 1:
                return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 0, 1,
                                           null_obstruct + front_null_obstruct)
            else:
                if null_chess_num == 1 or front_null_chess_num == 1:
                    return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 1, 0,
                                               null_obstruct + front_null_obstruct)
                else:
                    return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 0, 0,
                                               null_obstruct + front_null_obstruct)

        elif all_num == 2:
            if front_null_chess_num == 1 and null_null_chess_num == 1:  # * *  *
                return self.cal_line_grade(all_num, front_obstruct, 1, 0, front_null_obstruct)
            if null_chess_num == 1 and front_null_null_chess_num == 1:  # *  * *
                return self.cal_line_grade(all_num, obstruct, 1, 0, null_obstruct)
            if front_null_null_chess_num == 1 and null_null_chess_num == 1:  # *  *  *
                return self.cal_line_grade(all_num, obstruct, 0, 1, null_obstruct)
            if front_null_chess_num == 1 and null_chess_num == 1:  # * * *

                return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 2, 0,
                                           front_null_obstruct + null_obstruct)
            if front_null_chess_num1 == 1 or null_chess_num1 == 1:  # * * *
                return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 2, 0,
                                           front_null_obstruct + null_obstruct)
            if chess_num == 2:  # ***
                return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 0, 0,
                                           front_null_obstruct + null_obstruct)
            if front_null_chess_num == 1 or null_chess_num == 1:  # * **
                return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 1, 0,
                                           front_null_obstruct + null_obstruct)
            if front_null_chess_num == 2 or null_chess_num == 2:
                return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 1, 0,
                                           front_null_obstruct + null_obstruct)
            if front_null_null_chess_num == 1 or null_null_chess_num == 1:  # *  **
                return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 0, 1,
                                           front_null_obstruct + null_obstruct)
            if front_null_null_chess_num == 2 or null_null_chess_num == 2:
                return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 0, 1,
                                           front_null_obstruct + null_obstruct)

        elif all_num == 3:
            if front_null_null_chess_num == 1 and null_null_chess_num == 1:  # *  **  *
                return self.cal_line_grade(all_num, obstruct + front_obstruct, 0, 1,
                                           front_null_obstruct + null_obstruct)
            if chess_num == 0:

                if front_null_chess_num == 3 or null_chess_num == 3:  # *  ***
                    return self.cal_line_grade(all_num + 1, 0, 1, 0, 0)
                if front_null_chess_num == 2 or null_chess_num == 2:
                    if front_null_chess_num1 == 1:  # * ** *
                        return self.cal_line_grade(all_num, obstruct, 1, 0, null_obstruct)
                    if null_chess_num1 == 1:  # * ** *
                        return self.cal_line_grade(all_num, front_obstruct, 1, 0, front_null_obstruct)
                    if null_chess_num == 1:  # ** * *
                        return self.cal_line_grade(all_num, front_obstruct, 1, 0, front_null_obstruct)
                    if front_null_chess_num == 1:  # * * **
                        return self.cal_line_grade(all_num, obstruct, 1, 0, null_obstruct)
                if front_null_chess_num1 == 1 or null_chess_num1 == 1:  # * * *
                    return self.cal_line_grade(all_num, 0, 2, 0, 0)
                if front_null_chess_num1 == 2 or null_chess_num1 == 2:  # ** * *
                    return self.cal_line_grade(all_num, 0, 2, 0, 0)

            elif chess_num == 1:

                if front_null_null_chess_num == 1:  # *  ** *
                    return self.cal_line_grade(all_num, obstruct, 1, 0, 0)
                if null_null_chess_num == 1:  # * **  *
                    return self.cal_line_grade(all_num, front_obstruct, 1, 0, 0)
                if front_null_chess_num == 2 or null_chess_num == 2:  # ** **
                    return self.cal_line_grade(all_num + 1, 0, 1, 0, 0)
                if front_null_chess_num == 1 and null_chess_num == 1:  # * ** *
                    if obstruct + front_obstruct == 2:
                        return self.cal_line_grade(all_num, 1, 1, 0, 0)
                    else:
                        return self.cal_line_grade(all_num, 0, 1, 0, 0)
                if front_null_chess_num1 == 1:  # * * **
                    return self.cal_line_grade(all_num, obstruct, 1, 0, 0)
                if null_chess_num1 == 1:  # ** * *
                    return self.cal_line_grade(all_num, front_obstruct, 1, 0, 0)
                if front_null_null_chess_num == 2 or null_null_chess_num == 2:  # **  **
                    return self.cal_line_grade(all_num, 0, 0, 2, 0)
            elif chess_num == 2:
                if front_null_null_chess_num == 1:  # *  ***
                    return self.cal_line_grade(all_num, obstruct, 0, 0, null_obstruct)
                if null_null_chess_num == 1:  # ***  *
                    return self.cal_line_grade(all_num, front_obstruct, 0, 0, front_null_obstruct)
                if front_null_chess_num == 1 or null_chess_num == 1:  # * ***
                    return self.cal_line_grade(all_num + 1, 0, 1, 0, 0)
            elif chess_num == 3:  # ****
                return self.cal_line_grade(all_num + 1, obstruct + front_obstruct, 0, 0,
                                           front_null_obstruct + null_obstruct)

        else:
            if chess_num - front_chess_num + null_chess_num + null_null_chess_num \
                    >= front_chess_num + front_null_chess_num + front_null_null_chess_num:
                num = chess_num + null_chess_num + null_null_chess_num
                if null_null_chess_num == 1:
                    return self.cal_line_grade(num, obstruct, 0, 0, null_obstruct)
                if null_null_chess_num >= 2:
                    return self.cal_line_grade(3, 0, 0, 1, 0)
                if null_chess_num > 0:
                    if chess_num >= 3:
                        return self.cal_line_grade(num, front_obstruct, 0, 0, front_null_obstruct)
                    return self.cal_line_grade(num + 1, obstruct, 1, 0, null_obstruct)
                return self.cal_line_grade(num + 1, obstruct, 0, 0, null_obstruct)
            else:
                num = chess_num + front_null_chess_num + front_null_null_chess_num
                if front_null_null_chess_num == 1:
                    return self.cal_line_grade(num, front_obstruct, 0, 0, front_null_obstruct)
                if front_null_null_chess_num >= 2:
                    return self.cal_line_grade(3, 0, 0, 1, 0)
                if front_null_chess_num > 0:
                    if chess_num >= 3:
                        return self.cal_line_grade(num, obstruct, 0, 0, null_obstruct)
                    return self.cal_line_grade(num + 1, front_obstruct, 1, 0, front_null_obstruct)
                return self.cal_line_grade(num + 1, front_obstruct, 0, 0, front_null_obstruct)
        return 0

    def cal_line_grade(self, chess_num, obstruct, null_num, double_null_num, null_obstruct):
        if chess_num == 1:
            return 0
        elif chess_num == 2:
            if obstruct == 0:
                if double_null_num == 1:
                    return 8
                else:
                    if null_num == 1:
                        return 10
                    return 12
            elif obstruct == 1:
                return 4
            else:
                return 0
        elif chess_num == 3:
            if obstruct == 0:
                if null_num == 0:
                    if double_null_num == 0:
                        if null_obstruct == 2:
                            return 16
                        return 38
                    else:
                        return 16
                elif null_num == 1:
                    return 32
                elif null_num == 2:
                    return 16
            elif obstruct == 1:
                if double_null_num == 1:
                    return 16
                if null_obstruct == 1:
                    return 0
                return 16
            else:
                if double_null_num == 1:
                    return 16
                else:
                    return 0
        elif chess_num == 4:
            if obstruct == 2:
                return 0
            if obstruct == 0 and null_num == 0:
                return 256
            if null_num == 1:
                return 42
            return 48
        elif chess_num == 5:
            if null_num == 1:
                return 48

            return 1024
        elif chess_num > 5:
            return 1024

        return 0
