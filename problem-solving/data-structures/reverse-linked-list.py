"""
Complete the 'reversePrint' function below.
Reference;- https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
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
    while head_node:
        print(head_node.data)
        head_node = head_node.next

if __name__ == "__main__":
    llist_count = int(input("Enter integer number of llist elements: ").strip())
    llist = SinglyLinkedList()

    for values in enumerate(range(0, llist_count)):
        llist_ele = int(input("Enter integer element {0}: ".format(values[0])).strip())
        llist.insert_node(llist_ele)

    print("Llist before reversal:")
    print_llist(llist.head)
