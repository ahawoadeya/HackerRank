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

    def delete_node(self, key):
        """ function to delete a node at a specific position"""

        # store head node as temporary
        temp = self.head

        # if head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # search for key to be deleted, keep track of the previous node
        # as we need to change prev.next
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in llist
        if temp is None:
            return

        # unlink the node from llist
        prev.next = temp.next

        temp = None


    def print_list(self):
        """print list contents"""
        temp = self.head
        while temp:
            print("{0}".format(temp.data)),
            temp = temp.next

# driver code
if __name__ == '__main__':
    llist = LinkedList()

    llist_elements = int(input("Enter number of elements in the linked list: ").strip())
    for values in enumerate(range(0, llist_elements)):
        llist_ele = int(input("Enter llist integer {0}: ".format(values[0])).strip())
        llist.push(llist_ele)

    print("Linked list before deleting:")
    llist.print_list()

    key_to_delete = int(input("Enter key to delete: ").strip())
    llist.delete_node(key_to_delete)

    print("Linked list after deleting at position {0}: ".format(key_to_delete))
    llist.print_list()
