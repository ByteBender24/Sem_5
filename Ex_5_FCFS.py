class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.turnaround_time = 0
        self.waiting_time = 0
        self.completion_time = 0
        self.arrival_time = 0  # assuming all processes arrive at time 0 for simplicity

def fcfs_scheduling(processes):
    total_processes = len(processes)
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    # Calculate Completion Time, Waiting Time, and Turnaround Time for each process
    for p in processes:
        # Completion time for FCFS: Current time + burst time
        p.completion_time = current_time + p.burst_time
        # Turnaround Time: Completion Time - Arrival Time (assumed arrival time = 0 for all processes here)
        p.turnaround_time = p.completion_time - p.arrival_time
        # Waiting Time: Turnaround Time - Burst Time
        p.waiting_time = p.turnaround_time - p.burst_time
        
        # Update totals for averages
        total_waiting_time += p.waiting_time
        total_turnaround_time += p.turnaround_time

        # Update the current time for the next process
        current_time = p.completion_time

    # Calculate Average Waiting Time and Average Turnaround Time
    average_waiting_time = total_waiting_time / total_processes
    average_turnaround_time = total_turnaround_time / total_processes

    # Print Results
    print("Process ID\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for p in processes:
        print(f"{p.pid}\t\t{p.burst_time}\t\t{p.waiting_time}\t\t{p.turnaround_time}\t\t{p.completion_time}")

    print("\nAverage Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)
    print("Total Turnaround Time:", total_turnaround_time)
    print("Total Waiting Time:", total_waiting_time)


# Example usage
if __name__ == "__main__":
    # Example processes with (pid, burst_time)
    processes = [Process(1, 6), Process(2, 8), Process(3, 7), Process(4, 3)]
    
    # Perform FCFS Scheduling
    fcfs_scheduling(processes)
