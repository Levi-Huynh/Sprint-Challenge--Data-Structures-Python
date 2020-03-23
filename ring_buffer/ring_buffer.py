from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):  # adds elements to the buffer

        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)  # add to tail
            # print("item", item, "self.storage.head",
            # self.storage.head.value, self.storage.tail.value)
            # update curr =self.storage.head
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            print("start of append", "head: ", self.storage.head.value,
                  "tail: ", self.storage.tail.value, "item", item)
            removed = self.storage.head
            # remove LRU from head to free space
            self.storage.remove_from_head()
            print("whats head after remove from head", self.storage.head.value)
            # add MRU to tail
            self.storage.add_to_tail(item)
            # this always occurs when limit is reached, (head removed)
            if removed == self.current:
                print(" after add teim tail & removed == self.current",
                      "self.current:", self.current.value, "self.head:", self.storage.head.value, "removed:", removed.value)
                # if current was head, reassign to tail
                print("tail here", self.storage.tail.value)
                self.current = self.storage.tail
                print("new self.current if removed was == self.current",
                      self.storage.tail.value)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # #return all elements in buffer in a in a list, in their given order
        # except for non values, should not be included in list

        curr = self.current
        print("curr", self.current.value)
        # append current to list
        list_buffer_contents.append(curr.value)

        if curr.next:  # give variable name to curr.next
            next_curr = curr.next
        else:
            next_curr = self.storage.head  # if next var is none, assign to head

        while next_curr != curr:  # while next.cur isn't equal to self.current
            list_buffer_contents.append(
                next_curr.value)  # append the curr value
            if next_curr.next:  # iterate through to next if curr.next exists
                next_curr = next_curr.next
            else:
                next_curr = self.storage.head  # else declare bext_curr as head and append hedd value
            # print("list content", list_buffer_contents)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
