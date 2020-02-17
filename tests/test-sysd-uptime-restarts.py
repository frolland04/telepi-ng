#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import datetime
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
    print(output[0].decode('utf8'))

    p = subprocess.Popen(['/bin/systemctl', 'show', 'lightdm.service', '-p', 'NRestarts', '--value'], stdout=subprocess.PIPE)
    output = p.communicate()
    print(output[0].decode('utf8'))

    p = subprocess.Popen(['/bin/systemctl', 'show', 'lightdm.service', '-p', 'ExecMainStartTimestamp', '--value'], stdout=subprocess.PIPE)
    output = p.communicate()
    print(output[0].decode('utf8'))

    print("fin.")
