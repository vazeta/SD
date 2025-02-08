import threading

class Q_ok:
    def __init__(self):
        self.n = 0
        self.value_set = False
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
    
    def get(self):
        with self.condition:
            while not self.value_set:
                try:
                    self.condition.wait()
                except Exception:
                    print("InterruptedException caught")
            
            print(f"Got: {self.n}")
            self.value_set = False
            self.condition.notify()
            return self.n
    
    def put(self, n):
        with self.condition:
            while self.value_set:
                try:
                    self.condition.wait()
                except Exception:
                    print("InterruptedException caught")
            
            self.n = n
            self.value_set = True
            print(f"Put: {n}")
            self.condition.notify()

class Producer_ok(threading.Thread):
    def __init__(self, q):
        super().__init__(name="Producer")
        self.q = q
        self.start()
    
    def run(self):
        i = 0
        while i < 100:
            self.q.put(i)
            i += 1

class Consumer_ok(threading.Thread):
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
    q = Q_ok()
    Producer_ok(q)
    Consumer_ok(q)

if __name__ == "__main__":
    main() 