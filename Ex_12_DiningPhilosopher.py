import threading
import time

# Number of philosophers (and forks)
N = 5

# Semaphores to represent the forks
forks = [threading.Semaphore(1) for _ in range(N)]

# Mutex to print philosopher actions without interference
print_lock = threading.Lock()

class Philosopher(threading.Thread):
    def __init__(self, index):
        super().__init__()
        self.index = index

    def run(self):
        while True:
            self.think()
            self.eat()

    def think(self):
        with print_lock:
            print(f"Philosopher {self.index} is thinking.")
        time.sleep(2)

    def eat(self):
        left_fork = self.index
        right_fork = (self.index + 1) % N

        # To avoid deadlock, try to pick up the forks in a specific order
        # Pick up the lower indexed fork first to avoid circular wait
        if self.index % 2 == 0:
            first_fork, second_fork = left_fork, right_fork
        else:
            first_fork, second_fork = right_fork, left_fork

        # Pick up the first fork (lock the semaphore for the fork)
        forks[first_fork].acquire()
        with print_lock:
            print(f"Philosopher {self.index} picked up fork {first_fork}")

        # Pick up the second fork
        forks[second_fork].acquire()
        with print_lock:
            print(f"Philosopher {self.index} picked up fork {second_fork}")

        # Now that both forks are picked up, philosopher can eat
        with print_lock:
            print(f"Philosopher {self.index} is eating.")
        time.sleep(2)

        # Put down the forks after eating
        forks[first_fork].release()
        with print_lock:
            print(f"Philosopher {self.index} put down fork {first_fork}")
        
        forks[second_fork].release()
        with print_lock:
            print(f"Philosopher {self.index} put down fork {second_fork}")

# Create and start philosopher threads
philosophers = [Philosopher(i) for i in range(N)]
for philosopher in philosophers:
    philosopher.start()

# Wait for all philosophers to finish (they never do in this case)
for philosopher in philosophers:
    philosopher.join()
