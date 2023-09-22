file { '/tmp/school':
  ensure  => file,                # Ensure it's a file
  mode    => '0744',             # File permissions
  owner   => 'www-data',         # Owner
  group   => 'www-data',         # Group
  content => 'I love Puppet',    # Content
}

