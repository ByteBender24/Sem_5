from multiprocessing import shared_memory
import time


class Client:
    def __init__(self, memory_name, buffer_size):
        self.buffer_size = buffer_size
        self.memory_name = memory_name
        self.shm = None

    def connect(self):
        self.shm = shared_memory.SharedMemory(name=self.memory_name)
        print(f"Client connected to shared memory: {self.memory_name}")

    def send_message(self, msg):
        message_bytes = msg.encode('utf-8')
        self.shm.buf[:len(message_bytes)] = message_bytes

    def receive_message(self):
        msg_bytes = self.shm.buf[:self.buffer_size]
        response = msg_bytes.tobytes().decode('utf-8').strip("\x00")
        print(f"Client received: {response}")
        return response

    def disconnect(self):
        self.shm.close()


if __name__ == "__main__":

    MEMORY_NAME = "SHM"
    BUFFER_SIZE = 256

    client = Client(MEMORY_NAME, BUFFER_SIZE)
    client.connect()

    try:
        client.send_message("Hello from client")
        time.sleep(1)
        msg = client.receive_message()

    finally:
        client.disconnect()