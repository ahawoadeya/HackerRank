"""
Complete the 'insertNodeAtPosition' function below.
https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
"""

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insert_node_at_position(llist, data, position):
    """implementation"""

    # get the head
    head = llist

    # check if position is valid
    if position < 0:
        print("Invalid position!")

    # if position is at the beginning
    if position == 0:
        # initialize a new node
        new_node = SinglyLinkedListNode(data)
        # the next node to the new one should point to the head
        new_node.next = llist
        # the new node should now be the head
        head = new_node
    else:
        # keep iterating until position is zero
        while position >= 0:
            position -= 1

            if position == 0:
                new_node = SinglyLinkedListNode(data)
                new_node.next = llist.next
                llist.next = new_node
                break

            llist = llist.next
            if llist is None:
                break
        if position != 0:
            print("Position out of range!")
    return head
