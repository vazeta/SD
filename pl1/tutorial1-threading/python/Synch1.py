import threading
import time


class Callme1:
    def __init__(self):
        # Create a single shared lock for all threads
        self.lock = threading.Lock()
        
    def call(self, msg):
        with self.lock:
            print(f"[{msg}", end="")
            try:
                time.sleep(1)
            except Exception:
                print("Interrupted")
            print("]")


class Caller1(threading.Thread):
    def __init__(self, target, msg):
        threading.Thread.__init__(self)
        self.target = target
        self.msg = msg
        self.start()

    def run(self):
        self.target.call(self.msg)


if __name__ == "__main__":
    target = Callme1()
    ob1 = Caller1(target, "Hello")
    ob2 = Caller1(target, "World")
    ob3 = Caller1(target, "Synchronized")

    ob1.join()
    ob2.join()
    ob3.join()
