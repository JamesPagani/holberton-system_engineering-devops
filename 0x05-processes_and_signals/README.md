# 0x05. Processes and signals

This project covers the handling of Linux's shell signals via Bash commands.

## Contents

* 0-what_is_my_pid: A script that shows its own PID
* 1-list_your_processes: Displays ALL of the currently running processes
* 2-show_your_bash_pid: Shows all bash processes using **grep** and **1-list_your_processes**
* 3-show_your_bash_pid_made_easy: Shows all bash PIDs using **pgrep**
* 4-to_infinity_and_beyond: Displays To infinity and beyond, over and over until forced to stop
* 5-kill_me_now: Kills the task made by **4-to_infinity_and_beyond** via **kill**.
* 6-kill_me_now_made_easy: Kills the task made by **4-to_infinity_and_beyond** via **pkill**
* 7-highlander: Same as **4-to_infinity_and_beyond**, but can't be stopped with SIGTERM signal
* 8-beheaded_process: Kills the task made by **7-highlander**
