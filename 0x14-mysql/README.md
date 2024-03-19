## Description
This project focuses on MySQL database administration, including installation, configuration, replication setup, and backup strategies.

## Concepts
The primary concepts covered in this project include:
- Database administration
- MySQL setup and configuration
- Primary-replica cluster setup
- Database backup strategies
- Web stack debugging

## Learning Objectives
Upon completion of this project, you should be able to:
- Understand the main role of a database
- Explain the purpose of a database replica
- Implement and manage primary-replica replication for MySQL databases
- Develop robust database backup strategies
- Explain the importance of storing backups in different physical locations
- Perform necessary operations to ensure the effectiveness of database backup strategies

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A `README.md` file, at the root of the project folder, is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

## Tasks
### 0. Install MySQL
- Install MySQL 5.7.x on both web-01 and web-02 servers.

### 1. Let us in!
- Create a MySQL user named `holberton_user` on both web-01 and web-02, allowing access for replication status check.

### 2. If only you could see what I've seen with your eyes
- Create a database named `tyrell_corp` on web-01 and insert at least one entry into a table named `nexus6`.

### 3. Quite an experience to live in fear, isn't it?
- Create a new user `replica_user` on web-01 with appropriate permissions for replication.

### 4. Setup a Primary-Replica infrastructure using MySQL
- Configure MySQL primary on web-01 and MySQL replica on web-02.
- Enable replication for the `tyrell_corp` database.

### 5. MySQL backup
- Write a Bash script to generate a MySQL dump, compress it to a tar.gz archive, and store it with a timestamped filename.

## Repository Structure
- Directory: 0x14-mysql

## Author
This project is authored by Sylvain Kalache, co-founder at Holberton School.

## Deadline and Evaluation
- Project start: Mar 19, 2024 6:00 AM
- Project end: Mar 20, 2024 6:00 AM
- Checker release: Mar 19, 2024 12:00 PM
- An auto-review will be launched at the deadline.
