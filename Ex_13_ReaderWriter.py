import threading
import time

shared_var = 0
read_count = 0

mutex = threading.Semaphore(1)
wrt = threading.Semaphore(1)

class Writer(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        global shared_var, read_count
        global mutex, wrt

        for _ in range(3):
            wrt.acquire()

            print(f"Writer {self.name} is writing to resource: {shared_var}")
            shared_var += 1
            time.sleep(0.5)

            print(f"Writer {self.name} is releasing the resource.")
            wrt.release()

            time.sleep(1)

class Reader(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        global shared_var, read_count
        global mutex, wrt

        for _ in range(3):
            mutex.acquire()
            global read_count
            read_count += 1

            if read_count == 1:
                wrt.acquire()

            mutex.release()

            print(f"Reader {self.name} is reading resource: {shared_var}")
            time.sleep(1)

            mutex.acquire()
            read_count -= 1
            if read_count == 0:
                wrt.release()

            mutex.release()

            time.sleep(1)

readers = [Reader(i) for i in range(3)]
writers = [Writer(j) for j in range(2)]

for reader in readers:
    reader.start()

for writer in writers:
    writer.start()

for reader in readers:
    reader.join()

for writer in writers:
    writer.join()
