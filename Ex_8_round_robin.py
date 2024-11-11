class Process:
    def __init__(self, pid, burst_time, arrival_time=0):
        self.pid = pid
        self.burst_time = burst_time  # Total burst time required by the process
        self.remaining_burst_time = burst_time  # Time remaining for the process
        self.arrival_time = arrival_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

    def __str__(self):
        return str(self.pid)

def round_robin_scheduling(processes, time_quantum):
    queue = processes[:]  # Create a copy of processes
    current_time = 0
    total_processes = len(processes)
    total_waiting_time = 0
    total_turnaround_time = 0
    order = []
    while queue:
        p = queue.pop(0)  # Get the process at the front of the queue
        
        # Process executes for a time quantum or remaining time (whichever is smaller)
        time_to_execute = min(p.remaining_burst_time, time_quantum)
        p.remaining_burst_time -= time_to_execute
        current_time += time_to_execute
        
        
        # If the process has completed, calculate its turnaround and waiting time
        if p.remaining_burst_time == 0:
            p.completion_time = current_time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            total_waiting_time += p.waiting_time
            total_turnaround_time += p.turnaround_time
        else:
            # If the process is not complete, requeue it with remaining burst time
            queue.append(p)
            order.append(str(p.pid))

    # Calculate averages
    average_waiting_time = total_waiting_time / total_processes
    average_turnaround_time = total_turnaround_time / total_processes
    
    # Print Results
    print("Process ID\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for p in processes:
        print(f"{p.pid}\t\t{p.burst_time}\t\t{p.arrival_time}\t\t{p.waiting_time}\t\t{p.turnaround_time}\t\t{p.completion_time}")
    
    print("\nAverage Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)
    print("Total Turnaround Time:", total_turnaround_time)
    print("Total Waiting Time:", total_waiting_time)
    print ("->".join(order))

# Example usage
if __name__ == "__main__":
    # Example processes with (pid, burst_time, arrival_time)
    processes = [
        Process(1, 6, 0),
        Process(2, 8, 1),
        Process(3, 7, 2),
        Process(4, 3, 3)
    ]
    
    # Define time quantum
    time_quantum = 4
    
    # Perform Round Robin Scheduling
    round_robin_scheduling(processes, time_quantum)
