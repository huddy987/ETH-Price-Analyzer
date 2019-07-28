#!/bin/bash

# Run main for 120 seconds
python ./main.py &
main_pid=$!
sleep 120
kill $main_pid

# Run the logging software for 120 seconds
python ./logging/stat_logger.py &
logger_pid=$!
sleep 120
kill $logger_pid
