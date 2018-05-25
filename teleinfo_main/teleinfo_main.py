#!/usr/bin/python
# -*- coding: UTF-8 -*-


# *** Dépendances ***
import sys
import threading
import time

# *** Sous-modules ***
import DatabaseEngine
import TeleInfo
import TemperatureHumidityProvider
import RunningLcd


# ================================================================================
# NAME: TELEINFO
# AUTHORS: Frédéric ROLLAND, depuis une idée et un code original de Sébastien Joly
# DATE : 2017-12-23
# COMMENT: Collecteur de trames Télé-Information ERDF et des caractéristiques
# de l'environnement proche (température et humidité relative).
# Historisation en BDD et affichage tournant sur LCD.
# ================================================================================

file = __file__.split('/')[-1]


print("File:", file)
print("Runtime:", sys.version)
print("**** Bonjour tout le monde ! ****")

# =============================
# *** Programme principal ! ***
# =============================


# Démarrage de l'écran LCD
# ------------------------

try:
    lcd = RunningLcd.RunningLcdOutput()
except:
    print("Affichage LCD indisponible!")
    sys.exit(-1)

# Tentative de connexion à la base de données
# -------------------------------------------

try:
    dex = DatabaseEngine.SafeRequestExecutor()
except:
    print("Base de données indisponible!")
    lcd.items = {'ERREUR': 'Accès BDD', 'Démarrage': 'impossible'}
    sys.exit(-2)

# Tentative de connexion au port série
# ------------------------------------

try:
    ti = TeleInfo.MessageProcessor(dex)
except:
    print("Entrée série indisponible!")
    lcd.items = {'ERREUR': 'Accès Téléinfo', 'Démarrage': 'impossible'}
    sys.exit(-3)

# Température et humidité relative relevées périodiquement
# --------------------------------------------------------

try:
    thp = TemperatureHumidityProvider.TemperatureHumidityProvider(dex)
except:
    print("Mesure de l'environnement indisponible!")
    lcd.items = {'ERREUR': 'Accès T/H', 'Démarrage': 'impossible'}
    sys.exit(-4)

# Boucle de réception des messages
# --------------------------------

# Attente du démarrage de tous les composants
# et de l'approvisionnement des premières valeurs
time.sleep(30)

lcd.items.clear()

stop = False
while not stop:
    try:
        print(">>> go")

        # Récupérer les données et les transmettre là où c'est nécessaire
        t = thp.temperature
        h = thp.humidity

        # Appliquer à l'affichage
        lcd.items['T'] = t
        lcd.items['H'] = h

        # Appliquer à la base de données
        # ...

        # On se revoit dans 10s
        time.sleep(10)

    except:
        # En cas de souci, on quitte la boucle
        print(">>> INTERRUPTED !")
        dex.pool.notifySystemFatalCondition()
        stop = True

# Arrêt de la collecte Téléinfo ERDF
ti.close()

# Arrêt des mesures de l'environnement
thp.close()

# Libération de l'écran LCD
lcd.close()

# Libération de la BDD
dex.close()

# On s'en va maintenant
sys.exit(-5)
