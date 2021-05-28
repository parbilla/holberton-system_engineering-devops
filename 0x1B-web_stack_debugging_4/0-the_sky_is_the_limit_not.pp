#Fix Nginx failed requests
exec { 'increaseRequestsLimit':
command => 'sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin']
}