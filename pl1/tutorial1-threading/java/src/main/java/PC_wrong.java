class Q {
  int n;

  synchronized int get() {
    System.out.println("Got: " + n);
    notify();
    try {
      wait();
    } catch (InterruptedException e) {
      // TODO: handle exception
      System.out.println("algo correu mal\n");
    }
    return n;
  }

  synchronized void put(int n) {
    this.n = n;
    try {
      wait();
    } catch (InterruptedException e) {
      // TODO: handle exception
      System.out.println("algo correu mal\n");
    }
    System.out.println("Put: " + n);
    notify();
  }
}

class Producer implements Runnable {
  Q q;

  Producer(Q q) {
    this.q = q;
    new Thread(this, "Producer").start();
  }

  public void run() {
    int i = 0;
    while (i < 100) {
      q.put(i++);
    }
  }
}

class Consumer implements Runnable {
  Q q;

  Consumer(Q q) {
    this.q = q;
    new Thread(this, "Consumer").start();
  }

  public void run() {
    int i = 0;
    while (i < 100) {
      q.get();
      i++;
    }
  }
}

class PC_wrong {
  public static void main(String args[]) {
    Q q = new Q();
    new Producer(q);
    new Consumer(q);
  }
}