
class RecentCounter:

    def __init__(self):
        self.window = []
        self.l=0
    def ping(self, t: int) -> int:
        self.window.append(t)
        self.l+=1

        while(self.window[0]<t-3000):
            self.window.pop(0)
            self.l-=1
        return self.l


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)