# 0x08. Networking basics #1

## Overview

This project is a part of the ALX School's DevOps curriculum, focusing on Networking basics. The tasks are designed to help participants understand concepts related to IP addresses, localhost, and `/etc/hosts` file.

## Learning Objectives

At the end of this project, participants are expected to:

- Understand what localhost/127.0.0.1 is
- Know what 0.0.0.0 represents
- Comprehend the purpose of the `/etc/hosts` file
- Display active network interfaces on a machine

## Resources

Participants are encouraged to read or watch the following resources:

- What is localhost
- What is 0.0.0.0
- What is the hosts file
- Netcat examples

Participants are advised to refer to the manual pages of the following commands:

- ifconfig
- telnet
- nc (Netcat)
- cut

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file at the root of the project folder is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without any errors
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script is doing

### Quiz Questions

Participants are encouraged to take the quiz provided to reinforce their understanding of the covered topics.

## Tasks

### 0. Change your home IP

Write a Bash script that configures an Ubuntu server with the below requirements:

- localhost resolves to 127.0.0.2
- facebook.com resolves to 8.8.8.8

Example:

```bash
sylvain@ubuntu$ sudo ./0-change_your_home_IP

### 1 more mandatory and advanced taske
