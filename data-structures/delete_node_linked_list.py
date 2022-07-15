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


def get_node(data):
    """function to create and return a Node"""

    # allocating space
    new_node = Node(data)
    return new_node

def delete_node(head_node, position):
    """ function to delete a node at a specific position"""

    head = head_node

    if position < 0:
        print("Invalid position")

    if position == 0:
        head = head.next

    return head


def print_list(head_node):
    """print list contents"""
    while head_node is not None:
        print(' ' + str(head_node.data), end='')
        head_node = head_node.next
    print()

# driver code
if __name__ == '__main__':
    new_head = get_node(23)
    new_head.next = get_node(85)
    new_head.next.next = get_node(76)
    new_head.next.next.next = get_node(38)

    print("Linked list before deleting:", end='')
    print_list(new_head)

    position_to_delete = int(input("Enter position to delete: ").strip())
    new_head = delete_node(new_head, position_to_delete)

    print("Linked list after deleting at position {0}: ".format(position_to_delete))
    print_list(new_head)
