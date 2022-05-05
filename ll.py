# A pretty basic linked list implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # last node pointer be null

    def __str__(self):

        return f'<Node object, value = {self.value}>'

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def add_tail_node(self, value):
        """Appends a Node (value)"""
        current = self.head
        while current.next:  # finds last node by traversing entire list
            current = current.next
        current.next = Node(value)

    def add_head_node(self, value):
        """Adds a new node to start of list and returns new head, does not modify inplace (value)"""
        current = self.head
        new_node = Node(value)
        new_node.next = current
        self.head = new_node

    def insert(self, index, value):
        """Inserts Node(value) at index (index)"""
        if index == 0:
            self.add_head_node(value)
            return 

        current = self.head
        current_index = 0
        while current_index != index-1 and current:
            current = current.next
            current_index += 1
        if current:
            new_node = Node(value)
            node_after_insert = current.next
            current.next = new_node
            new_node.next = node_after_insert
        else:
            raise IndexError("End of list reached")

    def get_all_values(self):
        """Returns a list of all node values"""
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        
        return values

    def __str__(self):
        values = self.get_all_values()
        values = [str(value) for value in values]

        return ' -> '.join(values)

    def __len__(self):
        len = 0
        current = self.head
        while current:
            len += 1
            current = current.next
        
        return len



    
ll = LinkedList(0)
ll.add_tail_node(1)
ll.add_tail_node(2)
ll.add_head_node(3)
ll.add_tail_node(4)
print(ll) 

ll.insert(2, 42)
print(ll)
print(ll.get_all_values())
print(len(ll))

# 3 -> 0 -> 1 -> 2 -> 4
# 3 -> 0 -> 1 -> 2 -> 4 -> 42
# [3, 0, 42, 1, 2, 4]
# 6
