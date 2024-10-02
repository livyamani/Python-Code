class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def list(self):
        elements = []
        present = self.head
        while present:
            elements.append(present.data)
            present = present.next
        return elements

    # O(1) Time, O(1) Space
    def insert_at_beginning(self, data):        
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node
    
    # O(n) Time, O(1) Space
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # O(n) Time, O(1) Space
    def delete_node(self, data):
        current_node = self.head
        if current_node is None:  # Empty list
            return
        if current_node.data == data:  # Head node removal
            self.head = current_node.next
            return
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next:
            current_node.next = current_node.next.next

    # O(n) Time, O(1) Space
    def find_node(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    # O(n) Time, O(1) Space
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

class Stack:
    def __init__(self):
        self.head = None

    def list(self):
        elements = []
        present = self.head
        while present:
            elements.append(present.data)
            present = present.next
        return elements

    # O(1) Time, O(1) Space
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # O(1) Time, O(1) Space
    def pop(self):
        if not self.head:
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    # O(1) Time, O(1) Space
    def peek(self):
        if not self.head:
            return None
        return self.head.data

    # O(n^2) Time, O(n) Space (due to recursion stack)
    def sort_stack(self):
        if self.head is None:
            return
        temp = self.pop()
        self.sort_stack()
        self.insert_in_sorted_order(temp)

    # O(n) Time, O(n) Space (due to recursion)
    def insert_in_sorted_order(self, data):
        if self.head is None or self.peek() <= data:
            self.push(data)
        else:
            top = self.pop()
            self.insert_in_sorted_order(data)
            self.push(top)

class Queue:
    def __init__(self):
        self.head = None

    def list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    # O(n) Time, O(1) Space
    def enqueue(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # O(1) Time, O(1) Space
    def dequeue(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    # O(1) Time, O(1) Space
    def peek(self):
        if not self.head:
            return None
        return self.head.data

# Testing the implementation
print("------------------------------------------------------------------------------------")
print("Modules in Linked List\n 1. Inserting the data  \n2. Deleting the data  \n3. Finding the data \n4. Reversed List")
LL = LinkedList()
LL.insert_at_beginning(10)
LL.insert_at_beginning(11)
LL.insert_at_beginning(12)
print("The LinkedList is:", LL.list())
LL.insert_at_end(48)
print("After inserting the data at end:", LL.list())
LL.delete_node(11)
print("After deleting the data:", LL.list())
print("Finding the data 12:", LL.find_node(12))
LL.reverse()
print("Reversed List:", LL.list())

print("------------------------------------------------------------------------------------")
print("Modules in Stack\n1. Pop \n2. Push  \n3. Peek ")
print("Stack")
S = Stack()
S.push(22)
S.push(13)
S.push(404)
S.push(55)
print("Stack List is:", S.list())
print("Popped data:", S.pop())
print("After popping:", S.list())
print("Peeked data:", S.peek())
S.sort_stack()
print("Sorted Stack:", S.list())

print("------------------------------------------------------------------------------------")
print("Modules in Queue \n1. Enqueue  \n2. Dequeued \n3. Peek")
print("Queue")
Q = Queue()
Q.enqueue(23)
Q.enqueue(43)
Q.enqueue(53)
print("Queue List is:", Q.list())
print("Peeked data:", Q.peek())
print("Dequeued data:", Q.dequeue())
print("Queue after dequeue:", Q.list())
