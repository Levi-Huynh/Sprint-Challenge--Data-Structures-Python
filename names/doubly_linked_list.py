"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
# only moves in 1 direction, can't move forward


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)

    """
    1) Wrap the given value in a ListNode 
    2) and insert it after this node. 
    3)Note that this node could already
    have a next node it is point to.
    """

    def insert_after(self, value):
        # initiate self.next = curr_next #if current_next is none, self.next is none. #if want to insert 2 between 1h >3, curr_next=3
        current_next = self.next
        # here just makes new instance of ListNode, declare self.next as value #
        self.next = ListNode(value, self, current_next)
        if current_next:  # if no current_next dont need to run line
            current_next.prev = self.next  # next for curr_next = self.next
            # if inserting node after => the .prev of curr_next becomes self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev  # curr_prev = self.prev
        # self.next -> ListNode instance
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            # whats Cur_prev.next for prevvalue you want to insert = self.prev
            current_prev.next = self.prev
            # if inserting before => the .next of curr_next = self.prev
            # if curr_prev var exists, the .next value = will be the self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next  # next node is self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0  # convenient to have access

    def __len__(self):
        return self.length

    def print(self):
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
            print(curr_node)
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:  # think of cases
            self.head = new_node  # think of cases
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node  # head points to new node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:  # think of cases
            self.head = new_node  # think of cases
            self.tail = new_node
        else:
            new_node.prev = self.tail  # next andprev are managing pointers, not actual data
            self.tail.next = new_node
            self.tail = new_node  # tail points to new node /value

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # if self.tail is None:
            # return
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):  # new_node = ListNode(2) #when we remove, we want to preserve connections and head & tails pointer # dont need to search through to delete,
         # just reset pointers dont need to traverse (examine every node) or search(stop at target) 3easer to manage pointers thatn search for value
        self.length -= 1
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            #self.length -= 1
        elif self.head == node:
            self.head = node.next  # move head pointer over, then call node.delete()
            #self.length -= 1
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            #self.length -= 1
            node.delete()
        else:
            #self.length -= 1
            node.delete()
        # node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # if not self.head:
            # return

        current = self.head
        max_val = current.value

        while current is not None and max_val is not None:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val


"""
first_node = ListNode(100)
linked_list = DoublyLinkedList(first_node)
linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.add_to_head(3)
linked_list.add_to_tail(5)
linked_list.delete(first_node)
linked_list.remove_from_head()
linked_list.remove_from_tail()
linked_list.print()
print('--------')
print(len(linked_list))
"""
