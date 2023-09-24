# Set up server configuration with puppet
file { '~/.ssh/config':
  ensure => present,
  content => "Host 18.235.248.71\n
              HostName 18.235.248.71\n
              User ubuntu\n
              IdentityFile ~/.ssh/school\n
              PasswordAuthentication no\n",
}

