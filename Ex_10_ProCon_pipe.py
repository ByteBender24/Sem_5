import os
import time
import threading

# Creating a pipe (returns a pair of file descriptors, r for reading, w for writing)
r, w = os.pipe()

# Producer Thread
def producer():
    items_produced = 0
    counter = 0

    while items_produced < 5:
        counter += 1
        message = f"Item {counter}".encode()  # Convert message to bytes
        os.write(w, message)  # Write to pipe
        print(f"Producer produced: {counter}")
        time.sleep(1)  # Simulating time taken to produce
        items_produced += 1

# Consumer Thread
def consumer():
    items_consumed = 0

    while items_consumed < 5:
        message = os.read(r, 1024)  # Read from pipe (1024 is the max buffer size)
        if message:
            print(f"Consumer consumed: {message.decode()}")  # Decode from bytes to string
            time.sleep(2)  # Simulating time taken to consume
            items_consumed += 1

# Creating threads for producer and consumer
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Starting threads
consumer_thread.start()
producer_thread.start()

# Waiting for threads to complete
producer_thread.join()
consumer_thread.join()
