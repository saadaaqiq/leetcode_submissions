# https://leetcode.com/problems/design-linked-list

class MyLinkedList:

    def __init__(self):
        self.q = deque()

    def get(self, index: int) -> int:
        if self.q and index < len(self.q):
            return self.q[index]
        return -1   

    def addAtHead(self, val: int) -> None:
        self.q.appendleft(val)

    def addAtTail(self, val: int) -> None:
        self.q.append(val)        

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 < index < len(self.q):
            self.q.insert(index, val)
        elif index == len(self.q):
            self.q.append(val)
        elif index == 0:
            self.q.appendleft(val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 < index < len(self.q):
            for i in range(index, len(self.q) - 1):
                self.q[i] = self.q[i+1]
            self.q.pop()
        elif index == 0:
            self.q.popleft()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)