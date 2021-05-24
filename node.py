
class Node:
    # 初始化一个节点
    def __init__(self, x, y, grade):
        self.x = x       # 节点值
        self.y = y
        self.grade = grade
        self.child = []    # 子节点列表

    # 添加子节点
    def add_child(self, node):
        self.child.append(node)
