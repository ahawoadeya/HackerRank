"""
Approach to deleting a node in a linked list

1. Delete from beginning.
    - Point head to the next node
    head = head->next

2. Delete from the end
    - Point head to the previous element, i.e, last second element
    change next pointer to null

3. Delete from the middle
    - Traverse to element before the element to be deleted
    - Change next pointer to exclude the node from the chain

steps;- 

- Find the previous node of the node to be deleted.
- Change the next of the previous node.
- Free memory for the node to be deleted.
"""

class Node:
    """initialize node"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """implementation"""

    # initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """insert new node at the beginning"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, head_node, position):
        """ function to delete a node at a specific position"""

        head = head_node

        if position < 0:
            print("Invalid position")

        if position == 0:
            head = head.next

        return head


    def print_list(self, head_node):
        """print list contents"""
        while head_node is not None:
            print(' ' + str(head_node.data), end='')
            head_node = head_node.next
        print()

# driver code
if __name__ == '__main__':
    llist = LinkedList()

    llist_elements = int(input("Enter number of elements in the linked list: ").strip())
    for values in enumerate(range(0, llist_elements)):
        llist_ele = int(input("Enter llist integer {0}: ".format(values[0])).strip())
        llist.push(llist_ele)

    print("Linked list before deleting:", end='')
    llist.print_list(llist.head)

    position_to_delete = int(input("Enter position to delete: ").strip())
    new_head = llist.delete_node(llist.head, position_to_delete)

    print("Linked list after deleting at position {0}: ".format(position_to_delete))
    llist.print_list(new_head)
