#!/bin/bash

echo "Starting teleinfo data collection.."

# Configuration du port série pour la collecte Téléinfo ERDF
stty -F /dev/ttyAMA0 1200 sane evenp parenb cs7 -crtscts

# Dossiers importants
TELEINFO_ROOT_DIR=/home/pi/teleinfo
TELEINFO_MAIN_DIR=$TELEINFO_ROOT_DIR/teleinfo_main

# Mise en place de la BDD
mysql -uteleinfo -pti < $TELEINFO_ROOT_DIR/db/D_TELEINFO.sql

# Log du démarrage
echo "use D_TELEINFO ; INSERT into T_DBG_ENTRIES set DbgMessage = 'STARTING COLLECTION', DbgContext = 'teleinfo.sh', DbgTs = NOW() ;" >/tmp/log.sql
mysql -uteleinfo -pti < /tmp/log.sql

# Lancement du programme de collecte
export PYTHONPATH=$TELEINFO_ROOT_DIR/io
python3 $TELEINFO_MAIN_DIR/teleinfo_main.py
#->/dev/null 2>&1
