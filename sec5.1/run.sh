#!/bin/bash

# Define an array of parameters
deepsets=("1")
parms=("0.8")
ls=("5" "10")
bmod=1
fmod=0

CUDA_VISIBLE_DEVICES=0


# Function to handle termination signals
terminate_tasks() {
    echo "Terminating all background tasks..."
    kill 0  # Send SIGTERM to all processes in the current process group
    exit 1
}

# Trap termination signals (e.g., Ctrl+C)
trap terminate_tasks SIGINT SIGTERM


# Loop through each parameter combination and run the tasks in parallel
for deepset in "${deepsets[@]}"
do
   for parm in "${parms[@]}"
   do
      for l in "${ls[@]}"
      do
         # Generate a unique log file for each task
         log_file="log/deepset_${deepset}_parm_${parm}_fmod${fmod}_bmod${bmod}_l${l}.txt"

         echo "Running with --deepset $deepset --parm $parm --fmod $fmod --bmod $bmod --l $l. Logging to $log_file."

         # Run the task via SSH and redirect output to the log file
         python -u run_newcar.py --deepset $deepset --parm $parm --fmod $fmod --bmod $bmod --l $l> $log_file 2>&1 &
      done
   done
done

# Wait for all background processes to finish
wait

echo "All tasks are complete. Logs are available in the respective log files."


