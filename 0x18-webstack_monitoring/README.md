# 0x18. Webstack Monitoring

## Description
In this project, we will implement tools for monitoring our web stack, focusing on both application monitoring and server monitoring. This involves gathering data about running software and server performance to ensure they are behaving as expected and not overloaded.

## Learning Objectives
- Understand why monitoring is needed.
- Learn about the two main areas of monitoring: application and server monitoring.
- Understand the purpose of access logs and error logs for a web server such as Nginx.

## Resources
Read or watch:
- [What is server monitoring](https://www.datadoghq.com/blog/what-is-server-monitoring/)
- [What is application monitoring](https://www.datadoghq.com/blog/what-is-application-monitoring/)
- [System monitoring by Google](https://landing.google.com/sre/book/chapters/monitoring-distributed-systems.html)
- [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script is doing

### Servers Information
| Name            | Username | IP            | State   |
|-----------------|----------|---------------|---------|
| 514118-web-01   | ubuntu   | 100.26.230.116| running |
| 514118-web-02   | ubuntu   | 18.233.65.185 | running |
| 514118-lb-01    | ubuntu   | 52.87.252.170 | running |

## Tasks

### 0. Sign up for Datadog and install datadog-agent
- Sign up for a free Datadog account at https://www.datadoghq.com/.
- Use the US1 region.
- Install the Datadog agent on `web-01`.
- Create an application key.
- Copy-paste your DataDog API key and your DataDog application key into your Intranet user profile.
- Ensure that your server `web-01` is visible in Datadog under the hostname `XX-web-01`.

### 1. Monitor some metrics
- Set up monitors in the Datadog dashboard to track the number of read and write requests issued to the device per second.

### 2. Create a dashboard
- Create a new dashboard in Datadog with at least 4 widgets to visualize different metrics.
- Create a file `2-setup_datadog` with the `dashboard_id` on the first line.

## Repository
- GitHub Repository: [alx-system_engineering-devops](https://github.com/your_username/alx-system_engineering-devops)
- Directory: `0x18-webstack_monitoring`
