
class Binary_Search_Tree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Binary_Search_Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Binary_Search_Tree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)