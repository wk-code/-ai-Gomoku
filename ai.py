import copy
from node import Node

#I'm coming!

class AI:
    def __init__(self, settings):
        self.depth = 3
        self.turn = 1
        self.settings = settings
        if settings.player_turn == 1:
            self.turn = 2

    def get_result(self, map_list, black_chess, white_chess):
        map_temp = copy.deepcopy(map_list)
        root = Node(-1, -1, 0)
        self.depth_first_traversal(root, 1, map_temp)

    def depth_first_traversal(self, node, depth, map_temp):
        if depth <= self.depth:
            self.find_child_node(map_temp, node)
        else:
            node.grade = self.cal_grade(map_temp)
            return node.grade

        turn = self.turn
        if depth % 2 == 0:
            if self.turn == 1:
                turn = 2
            else:
                turn = 1
        temp_node = []

        if len(node.child) != 0:
            for ele in node.child.copy:
                map_temp[ele.x][ele.y] = turn
                grade = self.depth_first_traversal(ele, depth + 1, map_temp)
                if turn == 1 and grade >= node.grade:
                    if depth == 1:
                        if grade != node.grade:
                            temp_node.clear()
                        temp_node.append(ele)
                    node.grade = grade
                elif turn == 2 and grade <= node.grade:
                    if depth == 1:
                        if grade != node.grade:
                            temp_node.clear()
                        temp_node.append(ele)
                    node.grade = grade

                map_temp[ele.x][ele.y] = 0

        if depth == 1:
            pass

    def find_child_node(self, map_temp, node):
        effect = 4
        x_min = self.settings.min_x - effect if self.settings.min_x - effect < 0 else 0
        x_max = self.settings.max_x + effect if self.settings.max_x + effect > 14 else 14
        y_min = self.settings.min_y - effect if self.settings.min_y - effect < 0 else 0
        y_max = self.settings.max_y + effect if self.settings.max_y + effect > 14 else 14
        for i in range(x_min, x_max + 1):
            for j in range(y_min, y_max + 1):
                if map_temp[i][j] == 0:
                    new_node = Node(i, j, 0)
                    node.add_child(new_node)

    def cal_grade(self, map_list):
        score = 0
        for i in range(10, -1, -1):
            score += self.cal_grade_line(map_list, 0, i, 1, 1)
        for i in range(1, 11):
            score += self.cal_grade_line(map_list, i, 0, 1, 1)
        for i in range(15):  # |
            score += self.cal_grade_line(map_list, i, 0, 0, 1)
        for i in range(4, 15):
            score += self.cal_grade_line(map_list, i, 0, -1, 1)
        for i in range(1, 11):
            score += self.cal_grade_line(map_list, 14, i, -1, 1)
        for i in range(15):
            score += self.cal_grade_line(map_list, 0, i, 1, 0)
        return score

    def cal_grade_line(self, map_list, x, y, x_change, y_change):
        black_score = 0
        white_score = 0
        bfront_front_obstruct = False
        bfront_obstruct = False
        bchess_num = 0
        bnull_num = 0
        bback_obstruct = False
        bback_back_obstruct = False

        wfront_front_obstruct = False
        wfront_obstruct = False
        wchess_num = 0
        wnull_num = 0
        wback_obstruct = False
        wback_back_obstruct = False

        check_stat = 0

        while -1 < x < 15 and -1 < y < 15:






            x += x_change
            y += y_change

        return black_score - white_score
