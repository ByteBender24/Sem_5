import os
import subprocess
import sys
import time

def simulate_ls(file_path):
    print ("\n".join(os.listdir(file_path)))
    
def simulate_cat(file_path, *args):
    """Simulates the `cat` command with redirection."""
    print(f'\nSimulating cat command for file: {file_path}')
    
    # Handle redirection
    output_file = None
    append_mode = False
    
    for arg in args:
        if arg == '>':
            output_file = args[args.index(arg) + 1]
        elif arg == '>>':
            output_file = args[args.index(arg) + 1]
            append_mode = True

    start_time = time.time()
    
    try:
        if output_file:
            mode = 'a' if append_mode else 'w'
            with open(file_path, 'r') as file:
                content = file.read()
            with open(output_file, mode) as outfile:
                outfile.write(content)
            print(f'Content redirected to {output_file}, \nContent = {content}')
        else:
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)

        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Execution Time for cat: {execution_time:.2f} seconds')
    
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except Exception as e:
        print(f'An error occurred while handling the file: {e}')

def simulate_ps(*args):
    """Simulates the `ps` command with arguments."""
    print('\nSimulating ps command:')
    
    start_time = time.time()
    
    command = 'ps'
    if args:
        command += ' ' + ' '.join(args)
    
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
        end_time = time.time()
        
        # Print the output of the ps command
        print(result.stdout)
        
        execution_time = end_time - start_time
        print(f'Execution Time for ps: {execution_time:.2f} seconds')
    
    except subprocess.CalledProcessError as e:
        print(f'Command failed with return code {e.returncode}')
        print(f'Error Output:\n{e.stderr}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

def simulate_commands():
    # Adjust the paths as needed
    file_path = 'sample.txt'  # Example file for cat (change as needed)
    output_file = 'output.txt'  # Example output file (change as needed)

    # Simulate `cat` command with redirection
    simulate_cat(file_path, '>', output_file)  # Overwrite
    simulate_cat(file_path, '>>', output_file)  # Append

    # Simulate `ps` command with additional arguments
    simulate_ps('-aux')  # Pass arguments to ps command

if __name__ == "__main__":
    simulate_commands()