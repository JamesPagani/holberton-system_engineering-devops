# Creates a file in in /tmp with the message "I love Puppet".
file {'holberton':
  path    => '/tmp/holberton',
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet'
}
