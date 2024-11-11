class Process:
    def __init__(self, pid, burst_time, priority, arrival_time):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.arrival_time = arrival_time
        self.remaining_burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.start_time = -1  # Time when the process first starts executing


def preemptive_priority_scheduling(processes):
    # Sort processes by arrival time (then by priority in case of tie)
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    
    current_time = 0
    total_processes = len(processes)
    completed_processes = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    
    # List to store processes that are ready to execute (waiting in ready queue)
    ready_queue = []

    while completed_processes < total_processes:
        # Add processes that have arrived by current_time
        for p in processes:
            if p.arrival_time <= current_time and p not in ready_queue and p.remaining_burst_time > 0:
                ready_queue.append(p)

        if ready_queue:
            # Sort ready_queue by priority (ascending), the process with the highest priority comes first
            ready_queue.sort(key=lambda p: (p.priority, p.arrival_time))
            # Pick the process with the highest priority (lowest priority value)
            current_process = ready_queue[0]

            if current_process.start_time == -1:  # If the process has not started yet
                current_process.start_time = current_time

            # Execute the current process for 1 time unit
            current_process.remaining_burst_time -= 1
            current_time += 1

            # If the process finishes its burst, calculate completion time and remove it from ready queue
            if current_process.remaining_burst_time == 0:
                current_process.completion_time = current_time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                total_waiting_time += current_process.waiting_time
                total_turnaround_time += current_process.turnaround_time
                ready_queue.remove(current_process)
                completed_processes += 1

        else:
            # If no process is in the ready queue, increment time
            current_time += 1

    # Calculate averages
    average_waiting_time = total_waiting_time / total_processes
    average_turnaround_time = total_turnaround_time / total_processes
    
    # Print Results
    print("Process ID\tBurst Time\tPriority\tArrival Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for p in processes:
        print(f"{p.pid}\t\t{p.burst_time}\t\t{p.priority}\t\t{p.arrival_time}\t\t{p.waiting_time}\t\t{p.turnaround_time}\t\t{p.completion_time}")
    
    print("\nAverage Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)
    print("Total Turnaround Time:", total_turnaround_time)
    print("Total Waiting Time:", total_waiting_time)


# Example usage
if __name__ == "__main__":
    # Example processes with (pid, burst_time, priority, arrival_time)
    processes = [
        Process(1, 6, 2, 0),
        Process(2, 8, 1, 1),
        Process(3, 7, 3, 2),
        Process(4, 3, 4, 3)
    ]
    
    # Perform Preemptive Priority Scheduling
    preemptive_priority_scheduling(processes)
