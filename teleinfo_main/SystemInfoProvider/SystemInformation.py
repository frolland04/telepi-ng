#!/usr/bin/python
# -*- coding: UTF-8 -*-


# *** Dépendances ***
import datetime
import time
import subprocess
import os
import sys
import psutil  # -- besoin de 'sudo python3 -m pip install psutil'

# *** Sous-modules ***
import Debug  # Besoin de mon décorateur "log_func"


"""
Quelques fonctions pour récupérer des informations intéressantes sur le système.
"""


def dbg_msg(*args):
    """
    Hook to print (or not) debugging messages for this Python file.
    """
    dbg_msg('[DBG]', *args)


@Debug.log_func
def get_elapsed_time_since_bootup():
    """
    Retrieving boot time & get elapsed time
    """

    # Call 'uptime' command
    sp_cmd_uptime_boot_tm = ['/usr/bin/uptime', '--since']

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


@Debug.log_func
def get_service_restart_count(service_name):
    """
    Retrieving restart count for a systemd service
    """

    # Call 'systemctl' command
    sp_cmd_systemd_exec_nb = ['/bin/systemctl', 'show', service_name, '-p', 'NRestarts', '--value']

    p = subprocess.Popen(sp_cmd_systemd_exec_nb, stdout=subprocess.PIPE)
    output = p.communicate()
    dbg_msg('Restarted', output[0].decode('utf8').rstrip(), 'times')

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


@Debug.log_func
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

    # Build date & time returned by 'create_time' (process start time)
    ptm = time.localtime(output)
    dbg_msg(str(ptm))

    # Elapsed time
    elapsed = datetime.timedelta(seconds=(time.mktime(cdt) - time.mktime(ptm)))
    dbg_msg('**** Time elapsed since process start: ****', elapsed, '->', elapsed.days, 'd', elapsed.seconds, 's')

    return elapsed


# Pour essayer les fonctions de ce fichier Python.
# ------------------------------------------------
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
    sys.exit(-1)
