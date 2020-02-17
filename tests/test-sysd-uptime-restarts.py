#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import datetime
import time
import subprocess
import sys


# uptime --since
# 2020-02-16 22:03:30
#
# systemctl show teleinfo.service -p NRestarts --value
# 0
#
# systemctl show teleinfo.service -p ExecMainStartTimestamp --value
# Sun 2020-02-16 22:03:45 CET

if __name__ == "__main__":
    print("coucou!")

    p = subprocess.Popen(['/usr/bin/uptime', '--since'], stdout=subprocess.PIPE)
    output = p.communicate()
    print(type(output), output, type(output[0]), len(output[0]), 'bytes', 'decoded:', output[0].decode('utf8'))

    # Current date & time
    cdt = time.localtime()
    print(str(cdt))

    # Date & time returned by 'uptime --since' (boot time)
    utm = time.strptime(output[0].decode('utf8')[0:19], '%Y-%m-%d %H:%M:%S')
    print(str(utm))
    elapsed = datetime.timedelta(seconds=(time.mktime(cdt) - time.mktime(utm)))
    print('**** Time elapsed since bootup: ****', elapsed, '->', elapsed.days, 'd', elapsed.seconds, 's')

    p = subprocess.Popen(['/bin/systemctl', 'show', 'lightdm.service', '-p', 'NRestarts', '--value'], stdout=subprocess.PIPE)
    output = p.communicate()
    print('Restarted', output[0].decode('utf8'), 'times')

    p = subprocess.Popen(['/bin/systemctl', 'show', 'lightdm.service', '-p', 'ExecMainStartTimestamp', '--value'], stdout=subprocess.PIPE)
    output = p.communicate()
    print(type(output), output, type(output[0]), len(output[0]), 'bytes', 'decoded:', output[0].decode('utf8'))

    # Date & time returned by 'systemctl' (boot time)
    utm = time.strptime(output[0].decode('utf8')[0:27], '%a %Y-%m-%d %H:%M:%S %Z')
    print(str(utm))
    elapsed = datetime.timedelta(seconds=(time.mktime(cdt) - time.mktime(utm)))
    print('**** Time elapsed since service restart: ****', elapsed, '->', elapsed.days, 'd', elapsed.seconds, 's')

    print("fin.")
