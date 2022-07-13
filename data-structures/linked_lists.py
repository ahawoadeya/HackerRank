"""
Given pointer to the head node of a linked list, the task is to reverse the linked list.
We need to reverse the list by changing the links between nodes.

Iterative Method

1. Initialize three pointers prev as NULL, curr as head, and next as NULL.
2. Iterate through the linked list. In loop, do following.
    - Before changing next of current,
    - store next node
        next = curr->next
    - Now change next of current
    - This is where actual reversing happens
        curr->next = prev
    - Move prev and curr one step forward
        prev = curr
        curr = next

references;-
1. https://www.geeksforgeeks.org/reverse-a-linked-list/
2. https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=linked-lists
"""


class Node:
    """implementation"""

    # constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """implementation"""

    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverse(self):
        """Function to reverse the linked list"""
        prev = None
        current = self.head

        # iteration
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def push(self, new_data):
        """Function to insert a new node at the beginning"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        """utility function to print the linked list"""
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


# driver code
test_array = LinkedList()

# specify array length
arr_count = int(input("Enter number of array elements: ").strip())

# populate array
for values in enumerate(range(0, arr_count)):
    arr_ele = int((input("Enter element {0}: ".format(values[0]))))
    test_array.push(arr_ele)

print("Original Linked List:")
test_array.print_list()

test_array.reverse()

print("\nReversed Linked List:")
test_array.print_list()
