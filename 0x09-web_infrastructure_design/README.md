# 0x09. Web Infrastructure Design

## Description
This project focuses on designing web infrastructure and covers concepts related to DNS, monitoring, web servers, network basics, load balancers, and servers. The project is to be done in teams of 3 people (your team: Rasha Saeed, Randa Saeed) and must be completed within the specified time frame.

## Concepts
For this project, understanding the following concepts is essential:

- DNS
- Monitoring
- Web Server
- Network basics
- Load Balancer
- Server

## Resources
Make sure to read or watch the following resources:

- Network basics concept page
- Server concept page
- Web server concept page
- DNS concept page
- Load balancer concept page
- Monitoring concept page
- What is a database
- What’s the difference between a web server and an app server?
- DNS record types
- Single point of failure
- How to avoid downtime when deploying new code
- High availability cluster (active-active/active-passive)
- What is HTTPS
- What is a firewall

## Learning Objectives
By the end of this project, you should be able to:

- Draw a diagram covering the web stack you built with the sysadmin/devops track projects
- Explain the purpose of each component in the web infrastructure
- Understand system redundancy
- Know acronyms: LAMP, SPOF, QPS

## Copyright - Plagiarism
Be aware of copyright and plagiarism rules. You must come up with solutions for the tasks independently to meet the learning objectives. Plagiarism is strictly forbidden and may result in removal from the program.

## Requirements
- A README.md file at the root of the project folder is mandatory.
- Whiteboard each task, take a picture/screenshot of your diagram.
- Manually review each task and provide a screenshot of completion.
- Whiteboard each task in front of a mentor, staff, or student.
- Focus on answering what is asked; avoid unnecessary details unless requested.

## Tasks

### Task 0: Simple web stack
Design a one-server web infrastructure with a LAMP stack. Ensure it includes a web server (Nginx), application server, application files, and a MySQL database. Explain the roles and issues associated with each component.


### Task 1: Distributed web infrastructure
Design a three-server web infrastructure hosting www.foobar.com. Include two servers, a web server (Nginx), an application server, a load balancer (HAproxy), application files, and a MySQL database. Explain the addition of each element, distribution algorithm for the load balancer, and differences between Active-Active and Active-Passive setups.



### Task 2: Secured and monitored web infrastructure
Design a three-server web infrastructure for www.foobar.com with security measures, encrypted traffic, and monitoring. Add three firewalls, an SSL certificate, and monitoring clients. Explain the purpose of each addition and address potential issues.

