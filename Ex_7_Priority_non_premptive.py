class Process:
    def __init__(self, pid, burst_time, priority):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.arrival_time = 0  # assuming all processes arrive at time 0 for simplicity
        self.turnaround_time = 0
        self.waiting_time = 0
        self.completion_time = 0

def priority_scheduling(processes):
    # Sort processes by priority (ascending order, lower number = higher priority)
    processes.sort(key=lambda x: x.priority)
    
    total_processes = len(processes)
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    
    # Calculate Completion Time, Waiting Time, and Turnaround Time for each process
    for p in processes:
        # Completion time is current time + burst time (since it's non-preemptive)
        p.completion_time = current_time + p.burst_time
        # Turnaround Time: Completion Time - Arrival Time (assumed to be 0)
        p.turnaround_time = p.completion_time - p.arrival_time
        # Waiting Time: Turnaround Time - Burst Time
        p.waiting_time = p.turnaround_time - p.burst_time
        
        # Update totals for averages
        total_waiting_time += p.waiting_time
        total_turnaround_time += p.turnaround_time
        
        # Update current time for the next process
        current_time = p.completion_time
    
    # Calculate Average Waiting Time and Average Turnaround Time
    average_waiting_time = total_waiting_time / total_processes
    average_turnaround_time = total_turnaround_time / total_processes
    
    # Print Results
    print("Process ID\tBurst Time\tPriority\tWaiting Time\tTurnaround Time\tCompletion Time")
    for p in processes:
        print(f"{p.pid}\t\t{p.burst_time}\t\t{p.priority}\t\t{p.waiting_time}\t\t{p.turnaround_time}\t\t{p.completion_time}")
    
    print("\nAverage Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)
    print("Total Turnaround Time:", total_turnaround_time)
    print("Total Waiting Time:", total_waiting_time)


# Example usage
if __name__ == "__main__":
    # Example processes with (pid, burst_time, priority)
    processes = [Process(1, 6, 2), Process(2, 8, 1), Process(3, 7, 3), Process(4, 3, 4)]
    
    # Perform Non-Preemptive Priority Scheduling
    priority_scheduling(processes)
