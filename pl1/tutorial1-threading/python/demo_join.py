import threading
import time

class NewThread1(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        print(f"New thread: {self.name}")
        self.start()  # Start the thread

    def run(self):
        try:
            for i in range(3, 0, -1):
                print(f"{self.name}: {i}")
                time.sleep(1)
        except Exception as e:
            print(f"{self.name} interrupted.")
        print(f"{self.name} exiting.")

class DemoJoin:
    @staticmethod
    def main():
        ob1 = NewThread1("T1")
        ob2 = NewThread1("T2")
        ob3 = NewThread1("T3")
        print(f"T1 is alive: {ob1.is_alive()}")
        print(f"T2 is alive: {ob2.is_alive()}")
        print(f"T3 is alive: {ob3.is_alive()}")
        # wait for threads to finish
        try:
            print("Waiting for threads to finish.")
            ob1.join()
            ob2.join()
            ob3.join()
        except Exception as e:
            print("Main thread interrupted")
        print(f"T1 is alive: {ob1.is_alive()}")
        print(f"T2 is alive: {ob2.is_alive()}")
        print(f"T3 is alive: {ob3.is_alive()}")
        print("Main thread exiting.")

if __name__ == "__main__":
    DemoJoin.main()