#!/bin/bash

# This script demonstrates the use of variables, if statements, loops, and functions

# Assigning a value to a variable
my_var=10
echo "Initial value of my_var is: $my_var"

# Using an if-else statement
if [ $my_var -gt 5 ]; then
    echo "my_var is greater than 5."
else
    echo "my_var is less than or equal to 5."
fi

# A simple loop that prints numbers from 1 to 5
echo "Numbers from 1 to 5:"
for i in {1..5}; do
    echo "Number: $i"
done

# While loop that counts down
countdown=5
echo "Countdown from $countdown:"
while [ $countdown -gt 0 ]; do
    echo "$countdown..."
    ((countdown--))  # Decrease the countdown by 1
done
echo "Countdown complete!"

# Using a function
greet_user() {
    echo "Hello, $1!"  # $1 refers to the first argument passed to the function
}

# Calling the function
greet_user "Alice"

# A case statement (switch-like in other languages)
day_of_week=$(date +%A)  # Get the current day of the week
echo "Today is $day_of_week."
case $day_of_week in
    Monday)
        echo "Start of the week!"
        ;;
    Friday)
        echo "Almost weekend!"
        ;;
    Saturday|Sunday)
        echo "Weekend!"
        ;;
    *)
        echo "Just another day."
        ;;
esac

# End of script
echo "Script execution completed."
