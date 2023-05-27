# https://leetcode.com/problems/design-browser-history

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = homepage
        self.before = []
        self.after = collections.deque()

    def visit(self, url: str) -> None:
        self.before.append(self.cur)
        self.cur = url
        self.after.clear()

    def back(self, steps: int) -> str:
        i = 0 
        while i < steps and self.before:
            self.after.appendleft(self.cur)
            self.cur = self.before.pop()
            i += 1
        return self.cur

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.after:
            self.before.append(self.cur)
            self.cur = self.after.popleft()
            i += 1
        return self.cur


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)