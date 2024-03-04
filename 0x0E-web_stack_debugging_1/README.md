# 0x0E. Web stack debugging #1

**Project Dates:** March 4, 2024 - March 8, 2024

## Project Description
In this project, we will delve into web stack debugging, focusing on Nginx configuration issues. The tasks will involve debugging an Nginx installation that is not listening on port 80 and creating Bash scripts to automate the fixing process.

## Concepts
For this project, we expect you to look at these concepts:
- Network basics
- Web stack debugging

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- All Bash script files must be executable
- Your Bash scripts must pass Shellcheck without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing
- You are not allowed to use wget

## Tasks
### 0. Nginx likes port 80
Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.

**Requirements:**
- Nginx must be running and listening on port 80 of all the server’s active IPv4 IPs
- Write a Bash script that configures a server to meet the above requirements
