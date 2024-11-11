import os
import sys

def execute_script_b():
    """Executes Ex_3_exec_B.py using execvp"""
    try:
        # execvp requires the script name and arguments; sys.argv[0] is the script name
        # Use 'python' or 'python3' as the interpreter (depending on your environment)
        os.execvp("python3", ["python3", "Ex_3_exec_B.py"])
    except Exception as e:
        print(f"Error executing Ex_3_exec_B.py: {e}")

if __name__ == "__main__":
    print("Ex_3_exec_A.py is executing...")
    # Simulate some work here in Ex_3_exec_A.py
    print("Now executing Ex_3_exec_B.py via execvp.")
    
    # Execute Ex_3_exec_B.py
    execute_script_b()

