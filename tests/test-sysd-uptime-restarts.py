#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import datetime
import time
import subprocess
import sys


# Exemples de choses essayées en ligne de commande:
# -------------------------------------------------
# uptime --since
# 2020-02-16 22:03:30
#
# systemctl show teleinfo.service -p NRestarts --value
# 0
#
# systemctl show teleinfo.service -p ExecMainStartTimestamp --value
# Sun 2020-02-16 22:03:45 CET

sp_cmd_uptime_boot_tm = ['/usr/bin/uptime', '--since']
sysd_service_name = 'teleinfo.service'
sp_cmd_systemd_exec_nb = ['/bin/systemctl', 'show', sysd_service_name, '-p', 'NRestarts', '--value']
sp_cmd_systemd_exec_last_tm = ['/bin/systemctl', 'show', sysd_service_name, '-p', 'ExecMainStartTimestamp', '--value']


if __name__ == "__main__":
    print("BEGIN!")

    ###########################################
    # Retrieving boot time & get elapsed time #
    ###########################################

    # Call 'uptime' command
    p = subprocess.Popen(sp_cmd_uptime_boot_tm, stdout=subprocess.PIPE)
    output = p.communicate()
    print(type(output), output, type(output[0]), len(output[0]), 'bytes', 'decoded:', output[0].decode('utf8'))

    # Get current date & time
    cdt = time.localtime()
    print(str(cdt))

    # Build date & time returned by 'uptime'
    utm = time.strptime(output[0].decode('utf8')[0:19], '%Y-%m-%d %H:%M:%S')
    print(str(utm))

    # Elapsed time
    elapsed = datetime.timedelta(seconds=(time.mktime(cdt) - time.mktime(utm)))
    print('**** Time elapsed since bootup: ****', elapsed, '->', elapsed.days, 'd', elapsed.seconds, 's')

    ##################################################
    # Retrieving restart count for a systemd service #
    ##################################################

    # Call 'systemctl' command
    p = subprocess.Popen(sp_cmd_systemd_exec_nb, stdout=subprocess.PIPE)
    output = p.communicate()
    print('Restarted', output[0].decode('utf8'), 'times')

    ###########################################################################
    # Retrieving latest restart time for a systemd service & get elapsed time #
    ###########################################################################

    # Call 'systemctl' command
    p = subprocess.Popen(sp_cmd_systemd_exec_last_tm, stdout=subprocess.PIPE)
    output = p.communicate()
    print(type(output), output, type(output[0]), len(output[0]), 'bytes', 'decoded:', output[0].decode('utf8'))

    # Get current date & time
    cdt = time.localtime()
    print(str(cdt))

    # Build date & time returned by 'systemctl' (restart time)
    utm = time.strptime(output[0].decode('utf8')[0:27], '%a %Y-%m-%d %H:%M:%S %Z')
    print(str(utm))

    # Elapsed time
    elapsed = datetime.timedelta(seconds=(time.mktime(cdt) - time.mktime(utm)))
    print('**** Time elapsed since service restart: ****', elapsed, '->', elapsed.days, 'd', elapsed.seconds, 's')

    print("END.")
