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


def get_count(llist_head):
    """get the number of nodes in llist"""
    temp = llist_head
    count_ = 0

    # loop while end of llist
    while temp:
        count_ += 1
        temp = temp.next

    return count_

def compare_lists(llist1, llist2):
    """compare two linked lists"""
    llist_a = llist1
    llist_b = llist2
    truthy = None

    while (llist_a is not None and llist_b is not None):
        if llist_a.data != llist_b.data:
            truthy = False
            break

        llist_a = llist_a.next
        llist_b = llist_b.next

    truthy =  llist_a is None and llist_b is None

    if get_count(llist2) == get_count(llist2) and truthy:
        return 1

    return 0


def print_llist(head_node):
    """print llist contents"""
    temp = head_node
    while temp:
        print(str(temp.data))
        temp = temp.next

if __name__ == "__main__":
    llist_1_count = int(input("Enter integer number of llist1 elements: ").strip())
    llist_1 = SinglyLinkedList()

    for values in enumerate(range(0, llist_1_count)):
        llist_ele = int(input("Enter integer element {0}: ".format(values[0])).strip())
        llist_1.insert_node(llist_ele)

    print()

    llist_2_count = int(input("Enter integer number of llist2 elements: ").strip())
    llist_2 = SinglyLinkedList()

    for values in enumerate(range(0, llist_2_count)):
        llist_ele = int(input("Enter integer element {0}: ".format(values[0])).strip())
        llist_2.insert_node(llist_ele)

    print("Original llist1:")
    print_llist(llist_1.head)
    print()
    print("Original llist2:")
    print_llist(llist_2.head)
    print()
    print(compare_lists(llist_1.head, llist_2.head))
