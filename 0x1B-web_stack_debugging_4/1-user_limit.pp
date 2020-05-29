# change OS config
file { 'change os':
    ensure  => present,
    path    => '/etc/security/limits.conf',
    content => '#This file has been wiped hahaha'
}
