import time
from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')


class LRUCache:
    def __init__(self):
        self.storage = dict()
        self.order = DoublyLinkedList()
        self.size = 0

    def get(self, key):
        if key not in self.storage:
            return None
        # access dict by key
        node = self.storage[key]
        # move key to head for mru?
        # is the front or end the mru in has table
        self.order.move_to_end(node)
        print(node.value[1])
        return node.value[1]  # 1 b/c key value pair

    def set(self, key, value):
        # the key does exist #essentially though don't want 2 of same keys
        if key in self.storage:
            # If in self.storage, overwrite it
            node = self.storage[key]
            # update the value in storage
            node.value = (key, value)  # ? #sets the node.value {key: value}
            print(node, node.value)
            # move the existing node to the tail as MRU!! #not adding node, just move to end
            self.order.move_to_end(node)  # self.order = DoublyLinkedList()
            return  # what does that actually RETURN? <-just ends it

        # the key does not exist
        # create a node with the key
        # add node to tail of order DLL
        # explicityly notes storage key & value
        self.order.add_to_tail((key, value))  # add to tail
        # store key and value in storage
        self.storage[key] = self.order.tail  # sets the value to tail
        self.size += 1


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


myCache = LRUCache()  # import LRUCache class , to store key values in dict
for name in names_1:  # for all names in first file
    myCache.set(name, 1)  # set key to name, and value 1

for name in names_2:  # for all names in file 2
    if myCache.get(name) == None:  # Check if name exists as key in myCache.
        pass  # dont do anything if it doesn't exist in myCache
    else:
        # if not a unique name & exists in myCache, append to the duplicates list
        duplicates.append(name)

"""
# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
