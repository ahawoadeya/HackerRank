"""
Complete the compare_lists function below.
Reference;- https://www.hackerrank.com/challenges/compare-two-linked-lists/problem?isFullScreen=false
"""


class SinglyLinkedListNode:
    """Node class"""

    def __init__(self, node_data):
        """constructor to initialize the node object"""
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    """llist class"""

    def __init__(self):
        """constructor to initialize llist"""
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        """function to populate llist consecutively"""
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_llist(head_node):
    """print llist contents"""
    temp = head_node
    while temp:
        print(str(temp.data))
        temp = temp.next
