#!/usr/bin/env bash
#create a file in /tmp. whit Puppet
file { '/tmp/holberton':
    path    => '/tmp/holberton',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
  }
