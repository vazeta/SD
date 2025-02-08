import threading
import time


class Callme:
    def call(self, msg):
        print(f"[{msg}", end="")
        try:
            time.sleep(1)
        except Exception:
            print("Interrupted")
        print("]")


class Caller(threading.Thread):
    def __init__(self, target, msg):
        threading.Thread.__init__(self)
        self.target = target
        self.msg = msg
        self.start()

    def run(self):
        self.target.call(self.msg)


class Synch:
    def main(self):
        target = Callme()
        ob1 = Caller(target, "Hello")
        ob2 = Caller(target, "Synchronized")
        ob3 = Caller(target, "World")
        ob1.join()
        ob2.join()
        ob3.join()


if __name__ == "__main__":
    Synch().main()
