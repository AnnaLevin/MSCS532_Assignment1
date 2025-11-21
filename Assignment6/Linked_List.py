class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        temp = self.head
        if temp and temp.value == value:
            self.head = temp.next
            return

        while temp and temp.next:
            if temp.next.value == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
