class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.size = size

    def next(self, val: int) -> float:
        self.window.append(val)

        if len(self.window) > self.size:
            self.window.popleft()

        total_sum = 0
        for n in self.window:
            total_sum += n
        return total_sum / len(self.window)


        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)