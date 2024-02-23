# Configuration Management

This project aims to demonstrate proficiency in configuration management using Puppet. The Puppet manifests provided here are designed to manage system configurations efficiently and effectively.

## Background Context

During my tenure at SlideShare, I encountered a critical incident where an auto-remediation tool inadvertently caused significant downtime due to a bug in the code. This incident underscored the importance of robust configuration management practices, particularly in large-scale infrastructure environments.

## Requirements

### General

- All files are interpreted on Ubuntu 20.04 LTS.
- Files should end with a new line.
- A `README.md` file at the project's root is mandatory.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without errors.
- Puppet manifests must run without errors.
- Puppet manifests must start with a comment explaining their purpose.
- Puppet manifest files must use the `.pp` extension.

### Versioning

- Ubuntu 20.04 VMs should have Puppet 5.5 preinstalled.

### Installation Instructions

To install Puppet and Puppet-lint, follow these steps:

#### Install Puppet

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
#### Taske
3 taske
