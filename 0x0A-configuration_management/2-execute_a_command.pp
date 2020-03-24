# Kills a process called "killmenow"
exec {'pkill':
  command  => 'pkill killmenow',
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  provider => 'shell'
}
