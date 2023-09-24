# Set up server configuration with puppet
file { '/root/.ssh/config':
  ensure => present,
  content => "Host example-server\n
              HostName your_server_hostname\n
              User your_ssh_username\n
              IdentityFile ~/.ssh/school\n
              PasswordAuthentication no\n",
  owner => 'root',
  group => 'root',
  mode => '0600',
}

