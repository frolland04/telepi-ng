#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import datetime
import time
import subprocess
import sys
import os
import psutil


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

sp_cmd_uptime_boot_tm       = ['/usr/bin/uptime', '--since']
sysd_service_name           = 'dbus.service'  # -- ou 'dbus.service' par exemple
sp_cmd_systemd_exec_nb      = ['/bin/systemctl', 'show', sysd_service_name, '-p', 'NRestarts', '--value']
sp_cmd_systemd_exec_last_tm = ['/bin/systemctl', 'show', sysd_service_name, '-p', 'ExecMainStartTimestamp', '--value']


def dbg_msg(*args):
    """
    Hook to print (or not) debugging messages for this Python file.
    """
    print('[DBG]', *args)
    

def get_elapsed_time_since_bootup():
    """
    Retrieving boot time & get elapsed time
    """
    # Call 'uptime' command
    p = subprocess.Popen(sp_cmd_uptime_boot_tm, stdout=subprocess.PIPE)
    output = p.communicate()
    dbg_msg(type(output), output, type(output[0]), len(output[0]), 'bytes', 'decoded:', output[0].decode('utf8').rstrip())

    # Get current date & time
    cdt = time.localtime()
    dbg_msg(str(cdt))

    # Build date & time returned by 'uptime'
    utm = time.strptime(output[0].decode('utf8')[0:19], '%Y-%m-%d %H:%M:%S')
    dbg_msg(str(utm))

    # Elapsed time
    elapsed = datetime.timedelta(seconds=(time.mktime(cdt) - time.mktime(utm)))
    dbg_msg('**** Time elapsed since bootup: ****', elapsed, '->', elapsed.days, 'd', elapsed.seconds, 's')

    return elapsed


def get_service_restart_count():
    """
    Retrieving restart count for a systemd service
    """
    # Call 'systemctl' command
    p = subprocess.Popen(sp_cmd_systemd_exec_nb, stdout=subprocess.PIPE)
    output = p.communicate()
    dbg_msg('Restarted', output[0].decode('utf8').rstrip(), 'times')

    return int(output[0].decode('utf8'))


def get_service_latest_restart_elapsed_time():
    """
    Retrieving latest restart time for a systemd service & get elapsed time
    """
    # Call 'systemctl' command
    p = subprocess.Popen(sp_cmd_systemd_exec_last_tm, stdout=subprocess.PIPE)
    output = p.communicate()
    dbg_msg(type(output), output, type(output[0]), len(output[0]), 'bytes', 'decoded:', output[0].decode('utf8').rstrip())

    # Get current date & time
    cdt = time.localtime()
    dbg_msg(str(cdt))

    # Build date & time returned by 'systemctl' (restart time)
    utm = time.strptime(output[0].decode('utf8')[0:27], '%a %Y-%m-%d %H:%M:%S %Z')
    dbg_msg(str(utm))

    # Elapsed time
    elapsed = datetime.timedelta(seconds=(time.mktime(cdt) - time.mktime(utm)))
    dbg_msg('**** Time elapsed since service restart: ****', elapsed, '->', elapsed.days, 'd', elapsed.seconds, 's')

    return elapsed


def get_process_start_elapsed_time():
    """
    Retrieving elapsed time since current process startup
    """
    # Use 'psutil'
    p = psutil.Process(os.getpid())
    output = p.create_time()
    dbg_msg(type(output), output)

    # Get current date & time
    cdt = time.localtime()
    dbg_msg(str(cdt))

    # Build date & time returned by 'create_time' (start time)
    ptm = time.localtime(output)
    dbg_msg(str(ptm))

    # Elapsed time
    elapsed = datetime.timedelta(seconds=(time.mktime(cdt) - time.mktime(ptm)))
    dbg_msg('**** Time elapsed since process start: ****', elapsed, '->', elapsed.days, 'd', elapsed.seconds, 's')

    return elapsed


if __name__ == "__main__":
    print("BEGIN!")

    print('------- GET_ELAPSED_TIME_SINCE_BOOTUP -------')
    e = get_elapsed_time_since_bootup()
    print('RESULT', type(e), e)

    print('------- GET_SERVICE_RESTART_COUNT -------')
    i = get_service_restart_count()
    print('RESULT', type(i), i)

    print('------- GET_SERVICE_LATEST_RESTART_ELAPSED_TIME -------')
    e = get_service_latest_restart_elapsed_time()
    print('RESULT', type(e), e)

    print('------- GET_PROCESS_START_ELAPSED_TIME -------')
    e = get_process_start_elapsed_time()
    print('RESULT', type(e), e)

    print("END!")
    sys.exit(0)
