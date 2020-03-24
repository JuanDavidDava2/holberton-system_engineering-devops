#!/usr/bin/env bash
# Install puppet-lint
package { 'puppet-lint':
    ensure   => '2.1.1',
    provider => 'gem',
}
