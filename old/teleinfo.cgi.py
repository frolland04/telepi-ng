#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import MySQLdb
import datetime
import subprocess
import sys


# ---------------------------------------------
# Lecture des N lignes d'une table

def readTableRows(name, nb, order='', reverse=False):
    
    optOrderedBy = ''

    if order != '':
        optOrderedBy = ' order by ' + order
        if reverse:
            optOrderedBy += ' desc'

    sql = 'select * from ' + name + optOrderedBy + ' limit ' + str(nb)

    try:
        cs.execute(sql)
       
        s = cs.fetchall()
        d = cs.description

    except Exception as e:
        print('Unable to fetch data from table', name, '!<br><br>', e, '<br><br>')
        sys.exit(1)
       
    row_idx = 0
    hdr_idx = 0

    print('<table>')
    print('<th colspan=', len(d), '>Fetching', nb, 'data from table', name, '..</th>')
    print('<tr>')
    for hdr_idx in range(len(d)):
        print('<th>', d[hdr_idx][0], '</th>')
    print('</tr>')
        
    for row_idx in range(len(s)):
        print('<tr>')
        for hdr_idx in range(len(d)):
            print('<td>', s[row_idx][hdr_idx], '</td>')
        print('</tr>')
    
    print('</table>')
    print('<br>')
    return
    

# ---------------------------------------------
# Lecture d'une ligne de la table

def readTableUniqueRow(name):
    sql = 'select * from ' + name

    try:
        cs.execute(sql)
       
        s = cs.fetchall()
        d = cs.description

    except Exception as e:
        print('Unable to fetch data from table', name, '!<br><br>', e, '<br><br>')

    i = 0

    print('<table>')
    print('<th colspan=3>Fetching data. Table', name, '..</th>')

    while i < len(d):
        print('<tr>')
        print('<td>', i, '</td>')
        print('<td>', d[i][0], '</td>')
        print('<td>', s[0][i], '</td>')
        print('</tr>')
        i = i + 1
    
    print('</table>')
    print('<br>')
    return
        

# -----------------------------------------------------------
# Lecture du résultat unique d'une requête

def executeRequestUniqueValue(sql):
    try:
        cs.execute(sql)

        s = cs.fetchall()

    except Exception as e:
        print('Unable to fetch data !', '<br><br>', e)

    return s[0][0]


# -----------------------------------------------------------
# Programme principal de la 'cgi'

print('Content-type: text/html; charset=UTF-8\n\n')
print('<!DOCTYPE html>')
print("<html lang='eng'>")

print('<head>')
print("<meta http-equiv='Content-Type' content='text/html; charset=utf-8'/>")
print('<title>TeleInformation ERDF</title>')
print('</head>')

print('<body>')
print('<style>'
      'table, th, td'
      '{'
      '  border: 2px solid black;'
      '  border-collapse: collapse;'
      '  padding: 10px;'
      '}'
      'table tr:nth-child(even)'
      '{'
      '  background-color: #CCC;'
      '}'
      '</style>')

print('Bienvenue sur la page du resume de la collecte de donnees TeleInfo ERDF !<br><br>')


# Lecture de l'identification du système Linux
p = subprocess.Popen(['/bin/uname', '-snrom'], stdout=subprocess.PIPE)
output = p.communicate()
uname = bytes(output[0]).decode('ascii')

# Lecture 'modèle'
with open('/proc/device-tree/model', 'r') as f:
    model = f.readline()

# Lecture 'numéro de série'
with open('/proc/device-tree/serial-number', 'r') as f:
    sn = f.readline()

# Lecture 'uptime' sous forme de durée
with open('/proc/uptime', 'r') as f:
    secs = f.readline().split()[0]
    uptime = datetime.timedelta(seconds=float(secs)).days

# Lecture du nom de la machine sous forme de chaine
p = subprocess.Popen(['/bin/hostname'], stdout=subprocess.PIPE)
output = p.communicate()
hostname = bytes(output[0]).decode('ascii')

# Lecture de l'adresse IPv4 sous forme de chaine
p = subprocess.Popen(['/bin/hostname', '-I'], stdout=subprocess.PIPE)
output = p.communicate()
address = bytes(output[0]).decode('ascii')

# Lecture horloge DS3231 sous forme de chaine
p = subprocess.Popen(['/sbin/hwclock'], stdout=subprocess.PIPE)
output = p.communicate()
hwclock = bytes(output[0]).decode('utf8')

# Lecture horloge système sous forme de chaine
p = subprocess.Popen(['/bin/date'], stdout=subprocess.PIPE)
output = p.communicate()
sysclock = bytes(output[0]).decode('utf8')
 
# Connexion à la BDD
db = MySQLdb.connect('localhost', 'teleinfo', 'ti', 'D_TELEINFO')
cs = db.cursor()

print('<table>')
print('<th colspan=2>Histo buffer</th>')
print('<tr><td>Name</td><td>', hostname, '</td></tr>')
print('<tr><td>IP</td><td>', address, '</td></tr>')
print('<tr><td>Model ID</td><td>', model, '</td></tr>')
print('<tr><td>SN</td><td>', sn, '</td></tr>')
print('<tr><td>System ID</td><td>', uname, '</td></tr>')
print('<tr><td>Uptime (days)</td><td>', uptime, '</td></tr>')
print('<tr><td>DS3231 clock</td><td>', hwclock, '</td></tr>')
print('<tr><td>System clock</td><td>', sysclock, '</td></tr>')
print('<tr><td>Collected samples</td><td>', executeRequestUniqueValue('select count(*) from T_HISTO' ), '</td></tr>')
print('<tr><td>Table allocated (MB)</td><td>', executeRequestUniqueValue("SELECT round(((data_length + index_length) / 1024 / 1024), 2) FROM information_schema.TABLES WHERE table_schema = 'D_TELEINFO' AND table_name = 'T_HISTO'" ), '</td></tr>')
print('<tr><td>Global heap max (MB)</td><td>', executeRequestUniqueValue('select round(((@@max_heap_table_size) / 1024 / 1024), 2)' ), '</td></tr>')
print('</table>')
print('<br>')
    
readTableUniqueRow('T_COUNTERS')

readTableUniqueRow('T_TELEINFO_INST')
readTableUniqueRow('T_TEMP_INST')
readTableUniqueRow('T_RH_INST')
readTableUniqueRow('T_PA_INST')

readTableRows('T_HISTO', 5, 'TS', True)

readTableRows('T_TELEINFO_MIN', 5, 'TS_DATE', True)
readTableRows('T_TELEINFO_MAX', 5, 'TS_DATE', True)
readTableRows('V_TELEINFO_MIN_MAX', 5)

readTableRows('T_TEMP_MIN', 5, 'TS_DATE', True)
readTableRows('T_TEMP_MAX', 5, 'TS_DATE', True)
readTableRows('V_TEMP_MIN_MAX', 5)

readTableRows('T_RH_MIN', 5, 'TS_DATE', True)
readTableRows('T_RH_MAX', 5, 'TS_DATE', True)
readTableRows('V_RH_MIN_MAX', 5)

readTableRows('T_PA_MIN', 5, 'TS_DATE', True)
readTableRows('T_PA_MAX', 5, 'TS_DATE', True)
readTableRows('V_PA_MIN_MAX', 5)

readTableRows('T_DBG_ENTRIES', 10)

db.close()

print('</body>')
print('</html>')

