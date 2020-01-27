#!/bin/bash

# ----------------------------------------------------------------------------------------
# Script de lancement de la collecte Télé Information ENEDIS et toutes fonctions associées
# ----------------------------------------------------------------------------------------

echo "[TELEINFO] STARTING"

# Configuration du port série pour la collecte Téléinfo ERDF
stty -F /dev/ttyAMA0 1200 sane evenp parenb cs7 -crtscts

# Dossiers importants
TELEINFO_ROOT_DIR=/home/pi/teleinfo
TELEINFO_MAIN_DIR=$TELEINFO_ROOT_DIR/teleinfo_main

# Mise en place de la BDD
mysql -uteleinfo -pti < $TELEINFO_ROOT_DIR/db/D_TELEINFO.sql

# Log du démarrage en s'adressant directement à la BDD
echo "use D_TELEINFO ; INSERT into T_DBG_ENTRIES set DbgMessage = 'STARTING TELEINFO', DbgContext = 'teleinfo.sh', DbgTs = NOW() ;" >/tmp/log.sql
mysql -uteleinfo -pti < /tmp/log.sql

# Dossiers de modules Python supplémentaires
export PYTHONPATH=$TELEINFO_ROOT_DIR/io

# Lancement du programme de collecte
python3 $TELEINFO_MAIN_DIR/teleinfo_main.py #>/dev/null 2>&1

# Log de la fermeture en s'adressant directement à la BDD
echo "use D_TELEINFO ; INSERT into T_DBG_ENTRIES set DbgMessage = 'TERMINATED', DbgContext = 'teleinfo.sh', DbgTs = NOW() ;" >/tmp/log.sql
mysql -uteleinfo -pti < /tmp/log.sql

echo "[TELEINFO] TERMINATED"
