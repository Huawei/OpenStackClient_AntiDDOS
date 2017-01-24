Command Samples
===============

1. antiddos config

#. antiddos open (开启AntiDDos）

.. code:: console

    # open antiddos with IP
    $ openstack antiddos open 160.44.196.90 --enable-l7 --traffic-pos=1 --http-request-pos=1
            --cleaning-access-pos=1 --app-type=1

    # open antiddos with floating ip id
    $ openstack antiddos open 194bca90-9c23-43fb-b744-9d0bbd043a76 --enable-l7 --traffic-pos=1 --http-request-pos=1
            --cleaning-access-pos=1 --app-type=1


#. antiddos close (关闭AntiDDos）

.. code:: console

    # close antiddos with ip
    $ openstack antiddos close 160.44.196.90
    # close antiddos with floating ip id
    $ openstack antiddos close 194bca90-9c23-43fb-b744-9d0bbd043a76



#. antiddos show (查看AntiDDos）

.. code:: console

    # show antiddos with ip
    $ openstack antiddos show 160.44.197.150
    +---------------------+--------------------------------------+
    | Field               | Value                                |
    +---------------------+--------------------------------------+
    | Floating IP id      | 11427e0f-dc37-4319-a0e2-390e560fe116 |
    | floating ip address | 160.44.197.150                       |
    | network type        | EIP                                  |
    | status              | normal                               |
    +---------------------+--------------------------------------+

    # show antiddos with floating ip id
    $ openstack antiddos show 11427e0f-dc37-4319-a0e2-390e560fe116
    +---------------------+--------------------------------------+
    | Field               | Value                                |
    +---------------------+--------------------------------------+
    | Floating IP id      | 11427e0f-dc37-4319-a0e2-390e560fe116 |
    | floating ip address | 160.44.197.150                       |
    | network type        | EIP                                  |
    | status              | normal                               |
    +---------------------+--------------------------------------+

#. antiddos set (更新AntiDDos设置）

.. code:: console

    # update antiddos with ip
    $ openstack antiddos set 160.44.197.150 --disable-l7 --traffic-pos=2 --http-request-pos=2
        --cleaning-access-pos=2 --app-type=0


#. antiddos status list (查看AntiDDos状态列表）

.. code:: console

    $ openstack  antiddos status list -h
    usage: openstack antiddos status list [-h] [-f {csv,json,table,value,yaml}]
                                          [-c COLUMN] [--max-width <integer>]
                                          [--noindent]
                                          [--quote {all,minimal,none,nonnumeric}]
                                          [--status {normal,configging,notConfig,packetcleaning,packetdropping}]
                                          [--ip IP] [--limit LIMIT]
                                          [--offset OFFSET]

    List AntiDDos status

    optional arguments:
      -h, --help            show this help message and exit
      --status {normal,configging,notConfig,packetcleaning,packetdropping}
                            list AntiDDos with status
      --ip IP               list AntiDDos with the ip (eg: 110.110.)
      --limit LIMIT         return result limit
      --offset OFFSET       return result offset

    ......

    # list all antiddos status that **ip contains 160.44.197**
    $ openstack antiddos status list --ip=160.44.197
    +--------------------------------------+---------------------+--------------+-----------+
    | Floating IP id                       | floating ip address | network type | status    |
    +--------------------------------------+---------------------+--------------+-----------+
    | 11427e0f-dc37-4319-a0e2-390e560fe116 | 160.44.197.150      | EIP          | normal    |
    | 22b0d54b-ca21-402e-b4f6-fc59a347e8bc | 160.44.197.15       | EIP          | notConfig |
    | a07be473-26b1-4619-b50f-2b208889c992 | 160.44.197.151      | EIP          | notConfig |
    +--------------------------------------+---------------------+--------------+-----------+

    # list all antiddos status that **status is normal**
    $ openstack antiddos status list --status=normal
    +--------------------------------------+---------------------+--------------+--------+
    | Floating IP id                       | floating ip address | network type | status |
    +--------------------------------------+---------------------+--------------+--------+
    | 11427e0f-dc37-4319-a0e2-390e560fe116 | 160.44.197.150      | EIP          | normal |
    | 11ee0ec8-2b4f-438d-8235-dd22a3effa46 | 160.44.196.90       | EIP          | normal |
    +--------------------------------------+---------------------+--------------+--------+