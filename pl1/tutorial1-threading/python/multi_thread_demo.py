import threading
import time


class NewThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        print(f"New thread: {self.name}")
        self.start()  # Start the thread

    def run(self):
        try:
            for i in range(5, 0, -1):
                print(f"{self.name}: {i}")
                time.sleep(1)
        except Exception:
            print(f"{self.name} interrupted")
        print(f"{self.name} exiting.")


class MultiThreadDemo:
    @staticmethod
    def main():
        NewThread("Sporting")
        NewThread("Benfica")
        NewThread("Porto")
        try:
            time.sleep(1)
        except Exception:
            print("Main thread interrupted")
        print("Main thread exiting...")


if __name__ == "__main__":
    MultiThreadDemo.main()
