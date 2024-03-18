# README: 0x13. Firewall

## Description
This project focuses on configuring a firewall using `ufw` (Uncomplicated Firewall) on the `web-01` server to restrict incoming traffic while allowing specific TCP ports.

## Concepts
The primary concept covered in this project is **Web stack debugging**.

## Background Context
In this scenario, we need to set up a firewall on the `web-01` server using `ufw`. The firewall should block all incoming traffic except for specific TCP ports: 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP).

## Resources
- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_(computing))
- [Web stack debugging](https://intranet.hbtn.io/concepts/68)

## Installation and Configuration
### Prerequisites
Ensure you have `ufw` installed on the server.

### Steps
1. SSH into `web-01`.
2. Run the following commands to configure `ufw`:
```bash
sudo ufw default deny incoming
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp
sudo ufw enable
