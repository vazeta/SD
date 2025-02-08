import threading
import time


class Callme2:
    def call(self, msg):
        print(f"[{msg}", end="")
        try:
            time.sleep(1) 
        except Exception:
            print("Interrupted")
        print("]")


class Caller2: 
    #self is explicit, but could be ommited
    def __init__(self, target, msg):
        self.msg = msg
        self.target = target
        self.t = threading.Thread(target=self.run) 
        self.t.start()

    def run(self):
        with self.target.lock:  #equivalent to locking on an object synchronized(target)
            self.target.call(self.msg)


class Synch2:
    def main(self):
        target = Callme2()
        target.lock = threading.Lock()
        
        ob1 = Caller2(target, "Hello")
        ob2 = Caller2(target, "Synchronized")
        ob3 = Caller2(target, "World")
        
        # wait for threads to end
        try:
            ob1.t.join()
            ob2.t.join()
            ob3.t.join()
        except Exception:
            print("Interrupted")


if __name__ == "__main__":
    Synch2().main()
