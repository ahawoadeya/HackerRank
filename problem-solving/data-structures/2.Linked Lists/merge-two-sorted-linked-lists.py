"""
Complete the mergeLists function below.
Reference;- https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
"""

class SinglyLinkedListNode:
    """node class"""

    def __init__(self, node_data):
        """constructor class to initialize a node"""
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    """llist class"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        """function to populate llist consecutively"""
        node = SinglyLinkedListNode(node_data)

        # check if llist is empty
        if not self.head:
            # make new node the head
            self.head = node
        else:
            # if not empty, it means we have a tail
            # make next node after tail the new node
            self.tail.next = node

        # irregardless
        self.tail = node


def print_llist(head_node):
    """print llist contents"""
    temp = head_node
    while temp:
        print(str(temp.data))
        temp = temp.next


# driver code
if __name__ == "__main__":
    print()
    llist1_count = int(input("Enter number of elements for first llist: ").strip())
    llist1 = SinglyLinkedList()

    for values in enumerate(range(0, llist1_count)):
        llist_ele = int(input("Enter integer element {0}: ".format(values[0])).strip())
        llist1.insert_node(llist_ele)

    print("Original first llist:")
    print_llist(llist1.head)

    print()

    llist2_count = int(input("Enter number of elements for second llist: ").strip())
    llist2 = SinglyLinkedList()

    for values in enumerate(range(0, llist2_count)):
        llist_ele = int(input("Enter integer element {0}: ".format(values[0])).strip())
        llist2.insert_node(llist_ele)

    print("Original second llist:")
    print_llist(llist2.head)
