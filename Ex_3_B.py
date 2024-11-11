import os
import sys

def execute_script_a():
    """Executes Ex_3_exec_A.py using execvp"""
    try:
        # execvp requires the script name and arguments
        # Use 'python' or 'python3' as the interpreter (depending on your environment)
        os.execvp("python3", ["python3", "Ex_3_exec_A.py"])
    except Exception as e:
        print(f"Error executing Ex_3_exec_A.py: {e}")

if __name__ == "__main__":
    print("Ex_3_exec_B.py is executing...")
    # Simulate some work here in Ex_3_exec_B.py
    print("Now executing Ex_3_exec_A.py via execvp.")
    
    # Execute Ex_3_exec_A.py
    execute_script_a()
