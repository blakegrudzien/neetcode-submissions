class Website:
    def __init__(self, url, next = None, prev = None):
        self.url = url
        self.next = next
        self.prev = prev 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Website(homepage)
        self.current_page = self.homepage
        
        

    def visit(self, url: str) -> None:
        new_website = Website(url, None, self.current_page)
        self.current_page.next = new_website
        self.current_page = self.current_page.next
        

    def back(self, steps: int) -> str:
        while self.current_page != self.homepage and steps > 0:
            self.current_page = self.current_page.prev
            steps -=1
        return self.current_page.url
        

    def forward(self, steps: int) -> str:
        while self.current_page.next and steps > 0:
            self.current_page = self.current_page.next
            steps -=1
        return self.current_page.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)