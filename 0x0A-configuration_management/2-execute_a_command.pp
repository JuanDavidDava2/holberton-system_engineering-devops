#!/usr/bin/env bash
# kill a process killmenow
exec { 'killmenow':
    command  => 'pkill killmenow',
    provider => shell,
}
