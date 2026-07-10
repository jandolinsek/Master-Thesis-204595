#!/usr/bin/bash

# start and detach from shell job table
nohup my_command > ~/my_command.log 2>&1 &
disown


ps aux | grep my_command
tail -n 100 ~/my_command.log

jobs -l

kill PID
# wait a few seconds, then if still running:
kill -9 PID