# 0x17. Web Stack Debugging #3

## Description
This project focuses on debugging a Wordpress website running on a LAMP stack. The goal is to fix a 500 Internal Server Error returned by Apache using strace and then automate the fix using Puppet.

## Tasks
### 0. Strace is your friend
Using strace, we identify the issue causing Apache to return a 500 error and fix it using Puppet.

## Requirements
- Ubuntu 14.04 LTS
- All files should end with a new line
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Puppet manifests must run without error
- Puppet manifests files must end with the extension .pp
- Puppet v3.4 will be used for checking
- Install puppet-lint:

