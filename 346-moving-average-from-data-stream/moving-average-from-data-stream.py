class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
            self.sum += val
        else:
            self.sum -= self.window.popleft()
            self.window.append(val)
            self.sum += val

        return self.sum / len(self.window)


        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)