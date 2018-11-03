#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import datetime
import subprocess
import sys


# ---------------------------------------------
# Lecture des N lignes d'une table

def readTableRows( name, nb, order='', reverse=False ):
    
    optOrderedBy = ""

    if ( order != '' ):
       optOrderedBy = " order by " + order
	
       if ( reverse == True ):
          optOrderedBy += " desc"

    sql = "select * from " + name + optOrderedBy + " limit " + str( nb )

    try:
       cs.execute(sql)
       
       s = cs.fetchall()
       d = cs.description

    except:
       print "Unable to fetch data from table", name, "!<br><br>"
       sys.exit(1)
       
    row_idx = 0
    hdr_idx = 0

    print "<table>"
    print "<th colspan=", len(d), ">Fetching", nb, "data from table", name, "..</th>"
    print "<tr>"
    for hdr_idx in range(len(d)):
        print "<th>", d[hdr_idx][0], "</th>"    
    print "</tr>"
        
    for row_idx in range(len(s)):
        print "<tr>"
        for hdr_idx in range(len(d)):
            print "<td>", s[row_idx][hdr_idx], "</td>"    
        print "</tr>"
    
    print "</table>"
    print "<br>"
    return
    

# ---------------------------------------------
# Lecture d'une ligne de la table

def readTableUniqueRow( name ):
    sql = "select * from " + name

    try:
       cs.execute(sql)
       
       s = cs.fetchall()
       d = cs.description

    except:
       print "Unable to fetch data from table", name, "!<br><br>"

    i = 0

    print "<table>"
    print "<th colspan=3>Fetching data. Table", name, "..</th>"

    while i < len(d):
        print "<tr>"
        print "<td>", i, "</td>" 
        print "<td>", d[i][0], "</td>"
        print "<td>", s[0][i], "</td>"
        print "</tr>"
        i = i + 1
    
    print "</table>"
    print "<br>"
    return
        

# -----------------------------------------------------------
# Lecture du résultat unique d'une requête

def executeRequestUniqueValue( sql ):
    try:
       cs.execute(sql)

       s = cs.fetchall()
       
    except:
       print "Unable to fetch data !"

    return s[0][0]


# -----------------------------------------------------------
# Programme principal de la "cgi"

print "Content-type: text/html; charset=UTF-8\n\n"
print "<html>"
print "<head><title>"
print "TéléInformation ERDF"
print "</title></head>"
print "<body>"
print "<style>table, th, td { border: 2px solid black; border-collapse: collapse; padding: 10px; } </style>"

print "Bienvenue sur la page du résumé de la collecte de données TéléInfo ERDF !<br><br>"

# Lecture 'uptime' sous forme de durée
with open( '/proc/uptime', 'r' ) as f:
    secs = f.readline().split()[0]
    uptime = datetime.timedelta( seconds = float( secs ) )

# Lecture horloge DS3231 sous forme de chaine
p = subprocess.Popen( [ "/sbin/hwclock" ], stdout=subprocess.PIPE )
output = p.communicate()
hwclock = output[ 0 ]

# Lecture horloge système sous forme de chaine
p = subprocess.Popen( [ "/bin/date" ], stdout=subprocess.PIPE )
output = p.communicate()
sysclock = output[ 0 ]
 
# Connexion à la BDD
db = MySQLdb.connect( "localhost", "teleinfo", "ti", "D_TELEINFO" )
cs = db.cursor()

print "<table>"
print "<th colspan=2>Histo buffer</th>"
print "<tr><td>Uptime</td><td>", uptime, "</td></tr>"
print "<tr><td>DS3231 clock</td><td>", hwclock, "</td></tr>"
print "<tr><td>System clock</td><td>", sysclock, "</td></tr>"
print "<tr><td>Collected samples</td><td>", executeRequestUniqueValue( "select count(*) from T_TELEINFO_HISTO" ), "</td></tr>"
print "<tr><td>Table allocated (MB)</td><td>", executeRequestUniqueValue( 'SELECT round(((data_length + index_length) / 1024 / 1024), 2) FROM information_schema.TABLES WHERE table_schema = "D_TELEINFO" AND table_name = "T_TELEINFO_HISTO"' ), "</td></tr>"
print "<tr><td>Global heap max (MB)</td><td>", executeRequestUniqueValue( "select round(((@@max_heap_table_size) / 1024 / 1024), 2)" ), "</td></tr>"
print "</table>"
print "<br>"
    
readTableUniqueRow( "T_COUNTERS" )
readTableUniqueRow( "T_TELEINFO_INST" )
readTableUniqueRow( "T_TEMP_INST" )
readTableUniqueRow( "T_RH_INST" )
readTableUniqueRow( "T_PA_INST" )
readTableRows( "T_HISTO", 5, "TS", True )
readTableRows( "T_TELEINFO_MIN", 5, "TS_DATE", True )
readTableRows( "T_TELEINFO_MAX", 5, "TS_DATE", True )
readTableRows( "T_TEMP_MIN", 5, "TS_DATE", True )
readTableRows( "T_TEMP_MAX", 5, "TS_DATE", True )
readTableRows( "T_RH_MIN", 5, "TS_DATE", True )
readTableRows( "T_RH_MAX", 5, "TS_DATE", True )
readTableRows( "T_PA_MIN", 5, "TS_DATE", True )
readTableRows( "T_PA_MAX", 5, "TS_DATE", True )
readTableRows( "T_DBG_ENTRIES", 10 )

db.close()

print "</body>"
print "</html>"

