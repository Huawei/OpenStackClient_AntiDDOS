Command Samples
===============

1. antiddos config::

    $ openstack antiddos config
    +-------------------------+-----------------------------------------------------------------------------------------+
    | Field                   | Value                                                                                   |
    +-------------------------+-----------------------------------------------------------------------------------------+
    | Traffic limited list    | packet_per_second='2000', traffic_per_second='10', traffic_pos_id='1'                   |
    |                         | packet_per_second='6000', traffic_per_second='30', traffic_pos_id='2'                   |
    |                         | packet_per_second='10000', traffic_per_second='50', traffic_pos_id='3'                  |
    |                         | packet_per_second='15000', traffic_per_second='70', traffic_pos_id='4'                  |
    |                         | packet_per_second='20000', traffic_per_second='100', traffic_pos_id='5'                 |
    |                         | packet_per_second='25000', traffic_per_second='150', traffic_pos_id='6'                 |
    |                         | packet_per_second='35000', traffic_per_second='200', traffic_pos_id='7'                 |
    |                         | packet_per_second='50000', traffic_per_second='250', traffic_pos_id='8'                 |
    |                         | packet_per_second='70000', traffic_per_second='300', traffic_pos_id='9'                 |
    | HTTP limited list       | http_packet_per_second='100', http_request_pos_id='1'                                   |
    |                         | http_packet_per_second='150', http_request_pos_id='2'                                   |
    |                         | http_packet_per_second='240', http_request_pos_id='3'                                   |
    |                         | http_packet_per_second='350', http_request_pos_id='4'                                   |
    |                         | http_packet_per_second='480', http_request_pos_id='5'                                   |
    |                         | http_packet_per_second='550', http_request_pos_id='6'                                   |
    |                         | http_packet_per_second='700', http_request_pos_id='7'                                   |
    |                         | http_packet_per_second='850', http_request_pos_id='8'                                   |
    |                         | http_packet_per_second='1000', http_request_pos_id='9'                                  |
    |                         | http_packet_per_second='1500', http_request_pos_id='10'                                 |
    |                         | http_packet_per_second='2000', http_request_pos_id='11'                                 |
    |                         | http_packet_per_second='3000', http_request_pos_id='12'                                 |
    |                         | http_packet_per_second='5000', http_request_pos_id='13'                                 |
    |                         | http_packet_per_second='10000', http_request_pos_id='14'                                |
    |                         | http_packet_per_second='20000', http_request_pos_id='15'                                |
    | Connection limited list | cleaning_access_pos_id='1', new_connection_limited='10', total_connection_limited='30'  |
    |                         | cleaning_access_pos_id='2', new_connection_limited='20', total_connection_limited='100' |
    |                         | cleaning_access_pos_id='3', new_connection_limited='30', total_connection_limited='200' |
    |                         | cleaning_access_pos_id='4', new_connection_limited='40', total_connection_limited='250' |
    |                         | cleaning_access_pos_id='5', new_connection_limited='50', total_connection_limited='300' |
    |                         | cleaning_access_pos_id='6', new_connection_limited='60', total_connection_limited='500' |
    |                         | cleaning_access_pos_id='7', new_connection_limited='70', total_connection_limited='600' |
    |                         | cleaning_access_pos_id='8',new_connection_limited='80', total_connection_limited='700' |
    +-------------------------+-----------------------------------------------------------------------------------------+

#. antiddos open (开启AntiDDos）::

    # open antiddos with IP
    $ openstack antiddos open 160.44.196.90 --enable-l7 --traffic-pos=1 --http-request-pos=1
            --cleaning-access-pos=1 --app-type=1 --os-antiddos-endpoint-override=https://antiddos.eu-de.otc.t-systems.com
    Request Received, task id: 13f621cb-3dfa-4d96-9821-cd7d11fb15af

    # open antiddos with floating ip id
    $ openstack antiddos open 194bca90-9c23-43fb-b744-9d0bbd043a76 --enable-l7 --traffic-pos=1 --http-request-pos=1
            --cleaning-access-pos=1 --app-type=1 --os-antiddos-endpoint-override=https://antiddos.eu-de.otc.t-systems.com
    Request Received, task id: 13f621cb-3dfa-4d96-9821-cd7d11fb15af

#. antiddos close (关闭AntiDDos）::

    # close antiddos with ip
    $ openstack antiddos close 160.44.196.90 --os-antiddos-endpoint-override=https://antiddos.eu-de.otc.t-systems.com
    Request Received, task id: 13f621cb-3dfa-4d96-9821-cd7d11fb15af

    # close antiddos with floating ip id
    $ openstack antiddos close 194bca90-9c23-43fb-b744-9d0bbd043a76 --os-antiddos-endpoint-override=https://antiddos.eu-de.otc.t-systems.com
    Request Received, task id: 13f621cb-3dfa-4d96-9821-cd7d11fb15af

#. antiddos show (查看AntiDDos）::

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

#. antiddos set (更新AntiDDos设置）::


    # update antiddos with ip
    $ openstack antiddos set 160.44.197.150 --disable-l7 --traffic-pos=2 --http-request-pos=2
        --cleaning-access-pos=2 --app-type=0
    Request Received, task id: 13f621cb-3dfa-4d96-9821-cd7d11fb15af


#. antiddos task show (查看AntiDDos任务状态）::

    $ openstack antiddos task show 11427e0f-dc37-4319-a0e2-390e560fe116
    +--------------+---------+
    | Field        | Value   |
    +--------------+---------+
    | Task Status  | success |
    | Task Message |         |
    +--------------+---------+


#. antiddos status list (查看AntiDDos状态列表）::

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

#. antiddos status show (查看AntiDDos防护状态）::

    $ openstack antiddos status show 160.44.197.150
    +--------+--------+
    | Field  | Value  |
    +--------+--------+
    | status | normal |
    +--------+--------+


#. antiddos daily (查看AntiDDos防护流量）::


    $ openstack antiddos daily 160.44.197.150
    +---------------------+--------+------------+-----------+--------+------------+-----------+
    | Start Time          | BPS In | BPS Attack | BPS Total | PPS In | PPS Attack | PPS Total |
    +---------------------+--------+------------+-----------+--------+------------+-----------+
    | 2017-01-23 17:18:33 |      0 |          0 |           |      0 |          0 |           |
    | 2017-01-23 17:23:33 |      0 |          0 |           |      0 |          0 |           |
    | 2017-01-23 17:28:33 |      0 |          0 |           |      0 |          0 |           |
    | 2017-01-23 17:33:33 |      0 |          0 |           |      0 |          0 |           |
    | 2017-01-23 17:38:33 |      0 |          0 |           |      0 |          0 |           |
    | 2017-01-23 17:43:33 |      0 |          0 |           |      0 |          0 |           |
    | 2017-01-23 17:48:33 |      0 |          0 |           |      0 |          0 |           |
    | 2017-01-23 17:53:33 |      0 |          0 |           |      0 |          0 |           |
    | 2017-01-23 17:58:33 |      0 |          0 |           |      0 |          0 |           |
    | 2017-01-23 18:03:33 |      0 |          0 |           |      0 |          0 |           |
    ......

#. antiddos logs (查看AntiDDos异常事件）::

    # Could not get data in Current Env, will test later
    $ openstack antiddos logs 160.44.197.150 --limit=10


#. antiddos weekly (查看AntiDDos周防护统计情况）::

    $ openstack antiddos weekly
    +----------------------+-------------------------------------------------------------------------------------------------------------+
    | Field                | Value                                                                                                       |
    +----------------------+-------------------------------------------------------------------------------------------------------------+
    | DDOS intercept times | 6                                                                                                           |
    | Weekly data          | ddos_blackhole_times='0', ddos_intercept_times='0', max_attack_bps='0', max_attack_conns='0',               |
    |                      | period_start_date='2017-01-30 18:39:59'                                                                     |
    |                      | ddos_blackhole_times='0', ddos_intercept_times='0', max_attack_bps='0', max_attack_conns='0',               |
    |                      | period_start_date='2017-01-31 18:39:59'                                                                     |
    |                      | ddos_blackhole_times='0', ddos_intercept_times='0', max_attack_bps='0', max_attack_conns='0',               |
    |                      | period_start_date='2017-02-01 18:39:59'                                                                     |
    |                      | ddos_blackhole_times='0', ddos_intercept_times='0', max_attack_bps='0', max_attack_conns='0',               |
    |                      | period_start_date='2017-02-02 18:39:59'                                                                     |
    |                      | ddos_blackhole_times='0', ddos_intercept_times='0', max_attack_bps='0', max_attack_conns='0',               |
    |                      | period_start_date='2017-02-03 18:39:59'                                                                     |
    |                      | ddos_blackhole_times='0', ddos_intercept_times='1', max_attack_bps='121', max_attack_conns='0',             |
    |                      | period_start_date='2017-02-04 18:39:59'                                                                     |
    |                      | ddos_blackhole_times='0', ddos_intercept_times='0', max_attack_bps='0', max_attack_conns='0',               |
    |                      | period_start_date='2017-02-05 18:39:59'                                                                     |
    | top10                | floating_ip_address='160.44.196.90', times='6'                                                              |
    +----------------------+-------------------------------------------------------------------------------------------------------------+


#. antiddos alert

    $ openstack antiddos alert config show --os-antiddos-api-version=2
    +--------------+---------------------------------------------------------------------------------------------------------------------+
    | Field        | Value                                                                                                               |
    +--------------+---------------------------------------------------------------------------------------------------------------------+
    | Topic URN    | None                                                                                                                |
    | Display Name | None                                                                                                                |
    | Warn Config  | antiDDoS='False', back_doors='False', bruce_force='False', high_privilege='False', remote_login='False',            |
    |              | send_frequency='0', waf='False', weak_password='False'                                                              |
    +--------------+---------------------------------------------------------------------------------------------------------------------