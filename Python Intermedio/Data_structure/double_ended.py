class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.left = None
        self.right = None

    def push_left(self, value):
        new_node = Node(value)
        if self.left is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node

    def push_right(self, value):
        new_node = Node(value)
        if self.right is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node

    def pop_left(self):
        if self.left is None:
            raise IndexError("Deque is empty")
        value = self.left.value
        self.left = self.left.next
        if self.left:
            self.left.prev = None
        else:
            self.right = None
        return value

    def pop_right(self):
        if self.right is None:
            raise IndexError("Deque is empty")
        value = self.right.value
        self.right = self.right.prev
        if self.right:
            self.right.next = None
        else:
            self.left = None
        return value

    def print_deque(self):
        current = self.left
        while current:
            print(current.value)
            current = current.next


deque = Deque()
deque.push_right(1)
deque.push_right(2)
deque.push_left(0)
deque.print_deque()
print(deque.pop_right())
print(deque.pop_left())
deque.print_deque()