class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

    '''
    class Listnode:

        def __init__(self):
            self.key = key
            self.next = None
    '''

class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10 ** 4)]

    '''
    class MyHashSet:

        def __init__(self):
            self.set = [Listnode(0) for _ in range(10 ** 4)]

    '''

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next is not None:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    '''
    def add(self, key: int) -> None:
            cur = self.set[key % len(self.set)]
            while cur.next != None:
                if cur.next.key == key:
                    return
                cur = cur.next
            cur.next = Listnode(key)
    '''

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next is not None:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    '''
    def remove(self, key: int) -> None:
            cur = self.set[key%len(self.set)]
            while cur.next != None:
                if cur.next.key == key:
                    cur.next = cur.next.next
                cur = cur.next
    '''

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next is not None:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
    '''
        def contains(self, key: int) -> bool:
            cur = self.set[key % len(self.set)]
            while cur.next != None:
                if cur.next == key:
                    return True
                cur = cur.next
            return False
    '''       


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)