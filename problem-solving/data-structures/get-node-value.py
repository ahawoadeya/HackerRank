"""
Complete the 'getNode' function below.
Reference;- https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
"""

class SinglyLinkedListNode:
    """node class"""

    def __init__(self, node_data):
        """constructor to initialize node"""
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    """llist class"""

    def __init__(self):
        """constructor to initialize a llist"""
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        """function to populate llist consecutively"""
        node = SinglyLinkedListNode(node_data)

        # check if empty
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def get_node_value(head_node, node_position):
    """function to return the node value"""
    index = 0
    temp = head_node

    while temp:
        if index == node_position:
            return temp.data

        temp = temp.next
        index += 1

def print_llist(llist_head):
    """print llist contents"""
    while llist_head:
        print(str(llist_head.data))
        llist_head = llist_head.next

# driver code
if __name__ == "__main__":
    llist_count = int(input("Enter number of llist elements: ").strip())
    llist = SinglyLinkedList()

    for values in enumerate(range(0, llist_count)):
        llist_ele = int(input("Enter llist integer {0}: ".format(values[0])).strip())
        llist.insert_node(llist_ele)

    print("Original llist:")
    print_llist(llist.head)

    position_ = int(input("Enter position of the llist item: ").strip())
    print("Llist node value at position {0} is: {1}".format(position_, get_node_value(llist.head, position_)))
