from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # is it at capactiy?
        if len(self.storage) == self.capacity:
            # Yes? current = item
            self.current.value = item
                #identify new head
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = self.storage.head
            # No? add to end and identify new head
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # Edge case for no nodes
        if len(self.storage) == 0:
            return list_buffer_contents
        else:
            # loop to append each node value
            curr = self.storage.head
            while curr:
                if curr.value:
                    list_buffer_contents.append(curr.value)
                curr = curr.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
