import threading
import time


class Callme3:
    def call(self, msg):
        print(f"[{msg}", end="")
        try:
            time.sleep(1)
        except Exception:
            print("Interrupted")
        print("]")


class Caller3(threading.Thread):
    def __init__(self, target, msg):
        threading.Thread.__init__(self)
        self.target = target
        self.msg = msg
        self.start()

    def run(self):
        with threading.Lock():
            self.target.call(self.msg)


class Synch3:
    def main(self):
        target1 = Callme3()
        target2 = Callme3()
        target3 = Callme3()
        ob1 = Caller3(target1, "Hello")
        ob2 = Caller3(target2, "Synchronized")
        ob3 = Caller3(target3, "World")
        ob1.join()
        ob2.join()
        ob3.join()


if __name__ == "__main__":
    Synch3().main()
