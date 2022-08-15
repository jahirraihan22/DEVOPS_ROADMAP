process to change host name

    jahir@jahir-MS-7B89:/opt/vagrant_vm/bash_part$ vagrant ssh scriptbox
    [vagrant@localhost ~]$ sudo -i
    [root@localhost ~]# vi /etc/hostname
    [root@localhost ~]# hostname
    localhost.localdomain
    [root@localhost ~]# hostname scriptbox
    [root@localhost ~]# logout
    [vagrant@localhost ~]$ logout
    jahir@jahir-MS-7B89:/opt/vagrant_vm/bash_part$ vagrant ssh scriptbox
    Last login: Mon Aug 15 05:05:10 2022 from 10.0.2.2
    [vagrant@scriptbox ~]$ 




