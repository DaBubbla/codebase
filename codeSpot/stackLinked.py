# The program creates a stack and allows the user to perform push
# and pop operations on it.





# Create a class Node with instance vars data and next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a class Stack with instance var head
class Stack:
    def __init__(self):
        self.head = None
        # The var head points to the 1st element in the linked list

        # Define methods push and pop inside the class Stack
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        # The method pop returns the data of the node at the front of the linked list and removes
        # the node. It returns None if there are no nodes
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped


# Create an instance of Stack and present a menu to the user to perform ops on the stack
a_stack = Stack()
while True:
    print("push <value>")
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print("Popped value: ", int(popped))
    elif operation == 'quit':
        break