#!/usr/bin/python
# -*- coding: UTF-8 -*-

# *** Dépendances ***
import datetime
import time
import subprocess

# *** Sous-modules ***
import Debug  # Besoin de mon décorateur "log_func"


"""
Quelques fonctions pour récupérer des informations intéressantes sur le système.
"""


@Debug.log_func
def get_elapsed_time_since_bootup():
    """
    Retrieving boot time & get elapsed time
    """

    # Call 'uptime' command
    sp_cmd_uptime_boot_tm = ['/usr/bin/uptime', '--since']

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

    return elapsed


@Debug.log_func
def get_service_restart_count(service_name):
    """
    Retrieving restart count for a systemd service
    """

    # Call 'systemctl' command
    sp_cmd_systemd_exec_nb = ['/bin/systemctl', 'show', service_name, '-p', 'NRestarts', '--value']

    p = subprocess.Popen(sp_cmd_systemd_exec_nb, stdout=subprocess.PIPE)
    output = p.communicate()
    print('Restarted', output[0].decode('utf8'), 'times')

    return int(output[0].decode('utf8'))


@Debug.log_func
def get_service_latest_restart_elapsed_time(service_name):
    """
    Retrieving latest restart time for a systemd service & get elapsed time
    """

    # Call 'systemctl' command
    sp_cmd_systemd_exec_last_tm = ['/bin/systemctl', 'show', service_name, '-p', 'ExecMainStartTimestamp', '--value']

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

    return elapsed
