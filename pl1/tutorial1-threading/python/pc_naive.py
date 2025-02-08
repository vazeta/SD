import threading

class Q_naive:
    def __init__(self):
        self.n = 0
        self.value_set = False
    
    def get(self):
        while not self.value_set:
            pass  # Busy waiting
        print(f"Got: {self.n}")
        self.value_set = False
        return self.n
    
    def put(self, n):
        while self.value_set:
            pass  # Busy waiting
        self.n = n
        self.value_set = True
        print(f"Put: {n}")

class Producer_naive(threading.Thread):
    def __init__(self, q):
        super().__init__(name="Producer")
        self.q = q
        self.start()
    
    def run(self):
        i = 0
        while i < 100:
            self.q.put(i)
            i += 1

class Consumer_naive(threading.Thread):
    def __init__(self, q):
        super().__init__(name="Consumer")
        self.q = q
        self.start()
    
    def run(self):
        i = 0
        while i < 100:
            self.q.get()
            i += 1

def main():
    q = Q_naive()
    Producer_naive(q)
    Consumer_naive(q)

if __name__ == "__main__":
    main() 