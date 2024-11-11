import os
import time
import sys

def compute_sum(arr):
    return sum(arr)

def compute_product(arr):
    product = 1
    for num in arr:
        product *= num
    return product

def main():
    arr = [1, 2, 3, 4]
    print(f"Parent Process: PID = {os.getpid()}")   
    pid = os.fork()
    if pid == 0:
        print(f"Child Process: PID = {os.getpid()}, Parent PID = {os.getppid()}")
        time.sleep(2) 
        array_sum = compute_sum(arr)
        print(f"Child Process: Computed Sum = {array_sum}")
        sys.exit(0)
    else:
        print(f"Parent Process: Created Child with PID = {pid}")
        _, status = os.wait()
        print(f"Parent Process: Child Exit Status = {os.WEXITSTATUS(status)}")
        array_product = compute_product(arr)
        print(f"Parent Process: Computed Product = {array_product}")

if __name__ == "__main__":
    main()
