#!/usr/bin/env python3
import os

filename = r"C:\Users\froz9\OneDrive\Desktop\Labs2\Lbka3\tree.txt"

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.__value = value
        self.__left = left
        self.__right = right

    @property
    def value(self): return self.__value
    @value.setter
    def value(self, val): self.__value = val

    @property
    def left(self): return self.__left
    @left.setter
    def left(self, node): self.__left = node

    @property
    def right(self): return self.__right
    @right.setter
    def right(self, node): self.__right = node

    def print_preorder(self):
        print(self.value, end=" ")
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.value, end=" ")
        if self.right:
            self.right.print_inorder()

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)

    @staticmethod
    def create_tree_file(fname):
        tree_data = "8 4 2 1 3 6 5 7 12 10 9 11 14 13 15"
        with open(fname, "w") as f:
            f.write(tree_data)
        print(f"File '{fname}' created.")

    @staticmethod
    def build_from_file(fname):
        if not os.path.exists(fname):
            BinaryTree.create_tree_file(fname)
        with open(fname, "r") as f:
            values = f.read().split()
        values = [int(v) for v in values]
        root = BinaryTree(values[0])
        for v in values[1:]:
            root.insert(v)
        return root

    def get_height(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return 1 + max(left_height, right_height)

    def print_top_view(self):
        height = self.get_height()
        width = height * 14
        height_canvas = (2 ** height) * 2
        canvas = [[" "] * width for _ in range(height_canvas)]

        def place_node(x, y, text):
            for i in range(len(text) + 2):
                if 0 <= y < height_canvas and 0 <= x - 1 + i < width:
                    canvas[y][x - 1 + i] = " "
            for i, symbol in enumerate(text):
                if 0 <= y < height_canvas and 0 <= x + i < width:
                    canvas[y][x + i] = symbol

        def draw_line(x_start, y_start, x_end, y_end):
            dx = x_end - x_start
            dy = y_end - y_start
            steps = max(abs(dx), abs(dy))
            if steps == 0:
                return
            for i in range(1, steps):
                x = round(x_start + dx * i / steps)
                y = round(y_start + dy * i / steps)
                if 0 <= y < height_canvas and 0 <= x < width:
                    if canvas[y][x] == " ":
                        if dy == 0:
                            canvas[y][x] = "-"
                        elif (dx > 0 and dy < 0) or (dx < 0 and dy > 0):
                            canvas[y][x] = "/"
                        else:
                            canvas[y][x] = "\\"

        def traverse_left(node, x, y, horizontal_gap, vertical_gap):
            if node is None:
                return
            label = str(node.value)
            place_node(x - len(label) // 2, y, label)
            next_horizontal = max(horizontal_gap // 2, 3)
            next_vertical = max(vertical_gap // 2, 2)
            if node.left:
                left_x, left_y = x - next_horizontal, y - next_vertical
                draw_line(x, y, left_x, left_y)
                traverse_left(node.left, left_x, left_y, next_horizontal, next_vertical)
            if node.right:
                right_x, right_y = x - next_horizontal, y + next_vertical
                draw_line(x, y, right_x, right_y)
                traverse_left(node.right, right_x, right_y, next_horizontal, next_vertical)

        def traverse_right(node, x, y, horizontal_gap, vertical_gap):
            if node is None:
                return
            label = str(node.value)
            place_node(x - len(label) // 2, y, label)
            next_horizontal = max(horizontal_gap // 2, 3)
            next_vertical = max(vertical_gap // 2, 2)
            if node.left:
                left_x, left_y = x + next_horizontal, y - next_vertical
                draw_line(x, y, left_x, left_y)
                traverse_right(node.left, left_x, left_y, next_horizontal, next_vertical)
            if node.right:
                right_x, right_y = x + next_horizontal, y + next_vertical
                draw_line(x, y, right_x, right_y)
                traverse_right(node.right, right_x, right_y, next_horizontal, next_vertical)

        center_x = width // 2
        center_y = height_canvas // 2
        horizontal_gap = height * 4
        vertical_gap = height_canvas // 4

        label = str(self.value)
        place_node(center_x - len(label) // 2, center_y, label)

        if self.left:
            left_x = center_x - horizontal_gap
            draw_line(center_x, center_y, left_x, center_y)
            traverse_left(self.left, left_x, center_y, horizontal_gap // 2, vertical_gap)

        if self.right:
            right_x = center_x + horizontal_gap
            draw_line(center_x, center_y, right_x, center_y)
            traverse_right(self.right, right_x, center_y, horizontal_gap // 2, vertical_gap)

        for row in canvas:
            line = "".join(row).rstrip()
            if line.strip():
                print(line)


my_tree = BinaryTree.build_from_file(filename)

print("\nView from top:\n")
my_tree.print_top_view()