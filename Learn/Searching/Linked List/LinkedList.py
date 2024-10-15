# Basic Node in Linked List
class Node:
    pass


node1 = Node()
node2 = Node()
node3 = node1  # Node3 and Node1 has the same address


# Basic Node with data
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(5)
node1.data
node1.data = 10


# Complete Linked List
class LinkedList:
    def __init__(self):
        self.head = None


list1 = LinkedList()
list1.head = Node(2)
list1.head.next = Node(3)
list1.head.next.next = Node(4)
list1.head.data, list1.head.next.data, list1.head.next.next.data

# Linked List Functions


class Node:  # Node Creation
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):  # Head Pointer Creation
        self.head = None

    def append(self, data):  # Adding new Nodes
        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(data)

    def display(self):  # Displaying the Values
        if self.head is None:
            print("List is Empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next

    def length(self):
        len = 0
        if self.head is None:
            print("Linked List is Empty")
        else:
            current_node = self.head
            while current_node is not None:
                len = len + 1
                current_node = current_node.next
            print(f"Length of the Linked list is {len}")

    def get_element(self, pos):
        l = 0
        if self.head is None:
            print("Linked List is empty")
        else:
            current_node = self.head
            while current_node is not None:
                if l == pos:
                    print(current_node.data)
                    break
                else:
                    current_node = current_node.next
                    l = l + 1
            print("Element is not present")


list1 = LinkedList()  # Object of Linked List (Head)

list1.append(10)  # New Nodes
list1.append(20)
list1.append(30)
list1.append(40)

list1.display()
list1.length()
list1.get_element(2)
list1.get_element(6)

# Reversing a Linked List


def Reverse(list):
    if list.head is None:
        return "Empty Linked List"
    current_node = list.head
    prev_node = None

    while current_node is not None:
        next_node = current_node.next

        current_node.next = prev_node

        prev_node = current_node
        current_node = next_node
    list.head = prev_node


Reverse(list1)
list1.display()
