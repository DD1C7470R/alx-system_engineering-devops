# Set up server configuration with puppet
# Set up server configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 18.235.248.71
    HostName 18.235.248.71
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
