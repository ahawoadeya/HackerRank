"""
Approach: To insert data ata a specific position, the below algorithm would be followed:

1. Traverse the linked list upto position-1 nodes.
2. Once all the position-1 nodes are traversed, allocate memory and the given data
    to the new node
3. Point the next pointer of the new node to the next of current node
4. Point the next pointer of the current node to the new node
"""

class Node:
    """implementation"""

    def __init__(self, data):
        self.data = data
        self.next_node = None

def get_node(data):
    """function to create and return a Node"""

    # allocating space
    new_node = Node(data)
    return new_node

def insert_at_pos(head_node, position, data):
    """function to insert a node at a required position"""

    head = head_node

    # this condition to check whether the position given is valid or not
    if position < 1:
        print("Invalid position!")

    if position == 1:
        new_node = Node(data)
        new_node.next_node = head_node
        head = new_node
    else:
        # keep looping until the position is zero
        while position != 0:
            position -= 1

            if position == 1:
                # adding Node at required position
                new_node = get_node(data)

                # making the new Node point to the old Node at
                # the same position
                new_node.next_node = head_node.next_node

                # replacing head_node with new Node to the old Node
                # to point to the new Node
                head_node.next_node = new_node
                break

            head_node = head_node.next_node

            if head_node is None:
                break

        if position != 1:
            print("Position out of range!")
    return head

def print_list(head_node):
    """print contents of the linked list"""
    while head_node is not None:
        print(' ' + str(head_node.data), end='')
        head_node = head_node.next_node
    print()

# Driver Code
if __name__ == '__main__':
    # creating the list
    head = get_node(17)
    head.next_node = get_node(55)
    head.next_node.next_node = get_node(6)
    head.next_node.next_node.next_node = get_node(110)

    print("Linked list before insertion:", end='')
    print_list(head)

    # insert node to linked list
    data_to_insert = int(input("Enter integer to insert: ").strip())
    position_inserted_at = int(input("Enter position to insert at: ").strip())
    head_after_insertion = insert_at_pos(head, position_inserted_at, data_to_insert)

    print("Linked list after insertion of {0} at position {1}: ".format(data_to_insert, position_inserted_at), end='')
    print_list(head_after_insertion)
