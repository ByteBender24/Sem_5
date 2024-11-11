from multiprocessing import shared_memory
import time


class Server:

    def __init__(self, name, size):
        self.buffer_size = size
        self.shm = None
        self.name = name

    def start(self):
        self.shm = shared_memory.SharedMemory(
            name=self.name, size=self.buffer_size, create=True)
        print(f"Server started with shared memory name: {self.name}")

        try:
            while True:
                msg = self.read_message()
                if msg:
                    print(f"Server received: {msg}")
                    response = "Server_Acknowledged"
                    self.write_message(response)
                    print(f"Server sent response: {response}")
                    raise Exception("Error")
                time.sleep(1)
                    
        except:
            print("Shutting down")
        finally:
            self.shm.close()
            self.shm.unlink()

    def read_message(self):
        msg_bytes = self.shm.buf[:self.buffer_size]
        return_msg = msg_bytes.tobytes().decode('utf-8').strip("\x00")
        return return_msg

    def write_message(self, message):
        write_bytes = message.encode('utf-8')
        self.shm.buf[:len(write_bytes)] = write_bytes


if __name__ == "__main__":

    MEMORY_NAME = "SHM"
    BUFFER_SIZE = 256

    server = Server(MEMORY_NAME, BUFFER_SIZE)
    server.start()
