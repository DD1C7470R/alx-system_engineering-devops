# Set up server configuration with puppet
file { '/root/.ssh/config':
  ensure => present,
  content => "Host 18.235.248.71\n
              HostName 18.235.248.71\n
              User ubuntu\n
              IdentityFile ~/.ssh/school\n
              PasswordAuthentication no\n",
  owner => 'root',
  group => 'root',
  mode => '0600',
}

