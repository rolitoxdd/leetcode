class Page:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.back = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Page(homepage)
        self.current = self.head
        

    def visit(self, url: str) -> None:
        aux = Page(url)
        self.current.next = aux
        aux.back = self.current
        self.current = aux

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.back == None:
                break
            self.current = self.current.back
        return self.current.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next == None:
                break
            self.current = self.current.next
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)