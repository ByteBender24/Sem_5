import threading
import time


#Shared memory variables
CAPACITY = 3
BUFFER = ["_" for i in range(CAPACITY)]
in_index = 0
out_index = 0

#SEMAPHORES
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)

class Producer (threading.Thread):

    def run(self):

        global CAPACITY, BUFFER, in_index, out_index
        global empty, full, mutex

        items_produced = 0
        counter = 0

        while items_produced < 5:
            empty.acquire()
            mutex.acquire()

            counter += 1
            BUFFER[in_index] = counter
            in_index = (in_index + 1) % CAPACITY
            print ("Produced: ", counter, BUFFER)

            time.sleep(0.5)

            mutex.release()
            full.release()

            items_produced += 1

class Consumer(threading.Thread):

    def run(self):

        global CAPACITY, BUFFER, in_index, out_index
        global empty, full, mutex

        items_consumed = 0

        while items_consumed < 5:
            full.acquire()
            mutex.acquire()

            item = BUFFER[out_index]
            out_index = (out_index + 1) % CAPACITY
            print ("Consumed: ", item , BUFFER)

            time.sleep(0.5)

            mutex.release()
            empty.release()

            items_consumed += 1

consumer = Consumer()
producer = Producer()

consumer.start()
producer.start()

consumer.join()
producer.join()