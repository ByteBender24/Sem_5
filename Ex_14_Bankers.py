# Function to check if the system is in a safe state
def is_safe_state(available, max_claim, allocation, n, m):
    work = available.copy()
    finish = [False] * n
    safe_sequence = []
    
    while len(safe_sequence) < n:
        progress_made = False
        for i in range(n):
            if not finish[i]:  # Process i hasn't finished
                # Check if the process can proceed with the available resources
                if all(max_claim[i][j] - allocation[i][j] <= work[j] for j in range(m)):
                    # Allocate resources to this process
                    for j in range(m):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(i)
                    progress_made = True
                    break
        
        if not progress_made:
            # If no progress was made, the system is not in a safe state
            return False, []
    
    return True, safe_sequence

# Function to request resources for a process
def request_resources(process, request, available, allocation, max_claim, n, m):
    # Check if the request is valid
    if any(request[j] > max_claim[process][j] - allocation[process][j] for j in range(m)):
        raise ValueError("Request exceeds maximum claim")
    if any(request[j] > available[j] for j in range(m)):
        raise ValueError("Request exceeds available resources")

    # Temporarily allocate the resources
    available_temp = available.copy()
    allocation_temp = [row.copy() for row in allocation]
    for j in range(m):
        available_temp[j] -= request[j]
        allocation_temp[process][j] += request[j]

    # Check if the system will remain in a safe state after allocation
    safe, _ = is_safe_state(available_temp, max_claim, allocation_temp, n, m)
    if not safe:
        raise ValueError("Request leads to an unsafe state")
    
    # If safe, grant the request
    for j in range(m):
        available[j] -= request[j]
        allocation[process][j] += request[j]

# Example usage
if __name__ == "__main__":
    # Number of processes (n) and resources (m)
    n = 5  # number of processes
    m = 3  # number of resources

    # Available resources
    available = [3, 3, 2]

    # Maximum resource claim matrix (max_claim[i][j] is the maximum resources process i can request of resource j)
    max_claim = [
        [7, 5, 3],  # Process 0
        [3, 2, 2],  # Process 1
        [9, 0, 2],  # Process 2
        [2, 2, 2],  # Process 3
        [4, 3, 3],  # Process 4
    ]

    # Allocation matrix (allocation[i][j] is the number of resources process i has of resource j)
    allocation = [
        [0, 1, 0],  # Process 0
        [2, 0, 0],  # Process 1
        [3, 0, 2],  # Process 2
        [2, 1, 1],  # Process 3
        [0, 0, 2],  # Process 4
    ]

    # Check if the system is in a safe state
    safe, sequence = is_safe_state(available, max_claim, allocation, n, m)
    if safe:
        print("System is in a safe state.")
        print(f"Safe sequence: {sequence}")
    else:
        print("System is not in a safe state.")

    # Request resources for process 1 (for example)
    try:
        request = [1, 0, 2]  # Process 1 requests 1 unit of resource 0, 0 unit of resource 1, and 2 units of resource 2
        request_resources(1, request, available, allocation, max_claim, n, m)
        print("Request granted. Resources updated.")
    except ValueError as e:
        print(f"Request denied: {e}")
