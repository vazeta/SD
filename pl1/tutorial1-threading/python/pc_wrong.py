import threading

class Q:
    def __init__(self):
        self.n = 0
        self.lock = threading.Lock()

    def get(self):
        with self.lock:
            print("Got:", self.n)
            return self.n

    def put(self, n):
        with self.lock:
            self.n = n
            print("Put:", n)

class Producer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
        self.start()

    def run(self):
        i = 0
        while i < 100:
            self.q.put(i)
            i += 1

class Consumer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
        self.start()

    def run(self):
        i = 0
        while i < 100:
            self.q.get()
            i += 1

if __name__ == "__main__":
    q = Q()
    Producer(q)
    Consumer(q)
