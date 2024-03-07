# Project: readmy.me 0x10 - HTTPS SSL

## By: Sylvain Kalache, co-founder at Holberton School

### Weight: 1

### Project Timeline:
- Start: Mar 7, 2024, 6:00 AM
- End: Mar 8, 2024, 6:00 AM
- Checker Release: Mar 7, 2024, 12:00 PM
- Auto Review Deadline: Mar 8, 2024

### Concepts:
- DNS
- Web stack debugging

### Background Context:
The project aims to explore the consequences of not securing website traffic.

### Resources:
- What is HTTPS?
- The 2 main elements SSL provides
- HAProxy SSL termination on Ubuntu 16.04
- SSL termination
- Bash function
- `awk` and `dig` commands

### Learning Objectives:
Upon completion, you should be able to explain:
- The roles of HTTPS SSL
- The purpose of encrypting traffic
- What SSL termination means

### Requirements:
- Use editors: vi, vim, emacs
- Interpret files on Ubuntu 16.04 LTS
- End files with a new line
- Include a mandatory README.md
- Bash scripts must be executable
- Pass Shellcheck (version 0.3.7) without errors
- Use `#!/usr/bin/env bash` as the first line in Bash scripts
- Include comments explaining script functionality
- Must handle DNS configuration and web stack debugging

## Tasks:

### 0. World Wide Web
- Configure domain zones
- Write a Bash script to display information about subdomains

**Requirements:**
- Add subdomains: www, lb-01, web-01, web-02
- Bash script accepts domain and subdomain arguments
- Output format: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
- Use `awk` and at least one Bash function
- Ignore Shellcheck case SC2086

### 1. HAProxy SSL Termination
- Configure HAProxy for SSL termination
- Serve encrypted traffic for the subdomain www

**Requirements:**
- HAProxy listens on TCP port 443
- Accept SSL traffic
- Serve encrypted traffic returning / of your web server
- HAProxy config file provided as 1-haproxy_ssl_termination

Ensure HAProxy version is 1.5 or higher for SSL termination functionality.

## Repositories:
- GitHub: alx-system_engineering-devops
- Directory: 0x10-https_ssl
- Files: 0-world_wide_web, 1-haproxy_ssl_termination

