"""
Complete the 'deleteNode' function below.
Reference;- https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
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
        """constructor to initialize the llist"""
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        """function to populate llist successively"""
        node = SinglyLinkedListNode(node_data)

        # check if llist is empty
        if not self.head:
            # if empty, make the new node the head
            self.head = node
        else:
            # if not empty, add the new node at the tail
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

def delete_node(llist_head, position):
    """
    Given a reference to the head of a list
    and a position, delete the node at a given position
    """
    head = llist_head

    if head is None:
        return None

    if position < 0 or position > get_count(llist_head) - 1:
        print("Invalid position")
        return head

    # if deleting head node
    if position == 0:
        head = head.next
        return head

    # else
    index = 0
    current = head
    prev = head
    temp = head

    while current is not None:
        if index == position:
            temp = current.next
            break
        prev = current
        current = current.next
        index += 1

    prev.next = temp

    return head

def print_llist(head_node):
    """print llist contents"""
    while head_node:
        print(str(head_node.data))
        head_node = head_node.next

# driver code
if __name__ == "__main__":
    llist_count = int(input("Enter number of llist elements: ").strip())
    llist = SinglyLinkedList()

    for values in enumerate(range(0, llist_count)):
        llist_ele = int(input("Enter llist integer element {0}: ".format(values[0])).strip())
        llist.insert_node(llist_ele)

    print("Llist before deleting:")
    print_llist(llist.head)

    position_to_delete = int(input("Enter integer position to delete: ").strip())
    LLIST_COUNT = get_count(llist.head)

    new_head = delete_node(llist.head, position_to_delete)

    if position_to_delete > LLIST_COUNT - 1:
        print_llist(llist.head)
    else:
        print("Llist after deleting at position {0}".format(position_to_delete))
        print_llist(new_head)
