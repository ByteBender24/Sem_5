import os
import sys

def execute_command(command):
    pid = os.fork()
    if pid == 0:
        try:
            os.execvp(command[0], command)
        except OSError as e:
            print(f"Error executing command {command[0]}: {e}", file=sys.stderr)
            sys.exit(1)
    elif pid > 0:
        os.wait()
        print(f"Command '{' '.join(command)}' executed in child process.")
    else:
        print("Fork failed", file=sys.stderr)
        sys.exit(1)

def main():
    commands = [
        ["ls", "-l"],
        ["pwd"],
        ["echo", "Hello World"]
    ]

    for cmd in commands:
        execute_command(cmd)

if __name__ == "__main__":
    main()
