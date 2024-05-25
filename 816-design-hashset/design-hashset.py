class Node:
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.set = [Node() for i in range(10**4)]

    def hash(self, key):
        return key % len(self.set)

    def add(self, key: int) -> None:
        index = self.hash(key)
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.set[index]

        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)