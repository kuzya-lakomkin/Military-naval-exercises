import time


class Countdown:
    def __init__(self, max_time):
        self.max_time = max_time
        self.last_time = time.time()
        self.counted_time = 0

    def update(self) -> bool:
        self.counted_time = self.counted_time + time.time() - self.last_time

        print(self.counted_time, self.last_time, self.max_time - self.counted_time)

        if self.counted_time > self.max_time:
            return True

        self.last_time = time.time()

    def reset(self):
        self.counted_time = 0
        self.last_time = time.time()
