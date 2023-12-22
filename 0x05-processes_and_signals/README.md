# DevOps Project: Processes and Signals

## Project Overview

This DevOps project, titled "Processes and Signals," is part of the ALX System Engineering and DevOps curriculum. The project focuses on understanding processes, signals, and related concepts in the Linux environment. The project will run from Dec 22, 2023, 6:00 AM, to Dec 23, 2023, 6:00 AM. The checker for this project will be released at Dec 22, 2023, 12:00 PM. An auto review will be launched at the deadline.

## Author
**Sylvain Kalache**

## Project Weight
**1**

## Project Resources
Read or watch:
- [Linux PID](https://www.man7.org/linux/man-pages/man5/proc.5.html)
- [Linux process](https://man7.org/linux/man-pages/man7/proc.7.html)
- [Linux signal](https://man7.org/linux/man-pages/man7/signal.7.html)
- [Process management in Linux](https://www.kernel.org/doc/Documentation/sysctl/kernel.txt)
- [man or help](https://man7.org/linux/man-pages/man1/man.1.html):
  - ps
  - pgrep
  - pkill
  - kill
  - exit
  - trap

## Learning Objectives
By the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

## Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

### 0. What is my PID
- Write a Bash script that displays its own PID.
  ```bash
  sylvain@ubuntu$ ./0-what-is-my-pid
  4120
  sylvain@ubuntu$
and more 11 taske
