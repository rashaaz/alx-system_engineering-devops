#!/usr/bin/pup

# Puppet manifest to kill a process named killmenow using pkill

exec { 'pkill':
  provider => 'shell',
  command  => 'pkill -f killmenow',
}
