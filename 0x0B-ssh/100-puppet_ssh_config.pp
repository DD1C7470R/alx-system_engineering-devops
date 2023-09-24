# Set up server configuration with puppet
file_line { '~/.ssh/config':
  path => present,
  line => Host 18.235.248.71
          HostName 18.235.248.71
          User ubuntu
          IdentityFile ~/.ssh/school
          PasswordAuthentication no,
}

