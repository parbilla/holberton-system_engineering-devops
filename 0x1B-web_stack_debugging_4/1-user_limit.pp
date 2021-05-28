#Login with user and open file
exec { 'holbertonUserLimits':
     command => 'sed -i s/4/20/ /etc/security/limits.conf && sed -i s/5/50/ /etc/security/limits.conf',
      path   => ['/bin', '/usr/bin', '/usr/sbin']
}
