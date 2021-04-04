# Using Puppet to make changes to our configuration file
file_line {'Declare identity file':
    ensure   => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/holberton',
}
file_line {'Decline password authorization':
    ensure   => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    PasswordAuthentication no',
}