#!/bin/bash

# # Define an array of parameters
# deepsets=("0" "1")
# tops=("40" "50" "60" "70")
# l=15


# # Function to handle termination signals
# terminate_tasks() {
#     echo "Terminating all background tasks..."
#     kill 0  # Send SIGTERM to all processes in the current process group
#     exit 1
# }

# # Trap termination signals (e.g., Ctrl+C)
# trap terminate_tasks SIGINT SIGTERM

# # Loop through each parameter combination and run the tasks in parallel
# for deepset in "${deepsets[@]}"
# do
#    for top in "${tops[@]}"
#    do
#       # Generate a unique log file for each task
#       log_file="l${l}_deepset_${deepset}_top_${top}.txt"

#       echo "Running with --deepset $deepset, --top $top, --l $l . Logging to $log_file."

#       # Run the task locally, specifying the GPU, and log output
#       python -u run_arg.py --deepset "$deepset" --top "$top" --l "$l" > "$log_file" 2>&1 &
#    done
# done

# # Wait for all background processes to finish
# wait

# echo "All tasks are complete. Logs are available in the respective log files."


# python -u run_arg.py --deepset 1 --top 8 --l 5 > "8.log" 2>&1 &
# python -u run_arg.py --deepset 1 --top 10 --l 5 > "10.log" 2>&1 &

# python -u run_arg.py --deepset 1 --top 34 --l 10 > "34.log" 2>&1 &
python -u run_arg.py --deepset 1 --top 60 --l 15 > "60.log" 2>&1 &


wait

echo "All tasks are complete. Logs are available in the respective log files."
