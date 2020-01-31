# -*- coding: UTF-8 -*-

# Dépendances
# Sous-modules
import Debug  # Besoin de mon décorateur 'log_class_func'
import DatabaseEngine

# Pour le débogage
this_file = __file__.split('\\')[-1]


class SqlPool:
    """
    Cette classe est une collection de requêtes SQL exécutables sur la BDD. L'objet qui réalise les
    exécutions doit lui être confié, et posséder une méthode 'execute'. Sinon l'exécuteur par défaut
    'SafeRequestExecutor' est utilisé.
    """

    @Debug.log_class_func
    def __init__(self, ex=None):
        """
        Initialisation du 'SqlPool' : exécuteur de requêtes utilisé ensuite
        """
        if ex is not None:
            self.ex = ex
        else:
            self.ex = DatabaseEngine.SafeRequestExecutor(self)

    @Debug.log_class_func
    def __del__(self):
        """
        Nettoyage du 'SqlPool'
        """
        print('...')

    @Debug.log_class_func
    def close(self):
        """
        Fin propre du 'SqlPool'
        """
        print('...')

    @Debug.log_class_func
    def __enter__(self):
        """
        Entrée de zone, pour gestion de contextes
        """
        print('...')
        return self

    @Debug.log_class_func
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Sortie de zone, pour gestion de contextes
        """
        print('...')
        return False

    @Debug.log_class_func
    def notifyDatabaseConnected(self, context=''):
        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = 'DATABASE CONNECTED',
            DbgContext = %s,
            DbgTs = NOW() """,
            context
        )

    @Debug.log_class_func
    def notifyDatabaseClosing(self, context=''):
        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = 'CLOSING DATABASE',
            DbgContext = %s,
            DbgTs = NOW() """,
            context
        )

    @Debug.log_class_func
    def notifySystemFatalCondition(self, context=''):
        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = 'FATAL EXCEPTION, ABORTING',
            DbgContext = %s,
            DbgTs = NOW() """,
            context
        )

    @Debug.log_class_func
    def incrementCountRecvMsg(self, ts=0):
        """Incrémente le nombre de messages reçus (bons ou mauvais)
        et horodatage du dernier message reçu"""

        self.ex.execute(
            """ UPDATE T_COUNTERS set
            RecvMsgNbTotal = RecvMsgNbTotal + 1,
            RecvMsgLastTs = %s """,
            ts
        )

    @Debug.log_class_func
    def incrementCountRecvMsgOk(self):
        """
        Incrémente le nombre de messages reçus bons
        """
        self.ex.execute(""" UPDATE T_COUNTERS set RecvMsgNbOK = RecvMsgNbOK + 1 """)

    @Debug.log_class_func
    def getCountRecvMsgOk(self):
        """
        Récupère le nombre de messages reçus bons
        """
        return self.ex.execute_request_for_simple_value(""" SELECT RecvMsgNbOK FROM T_COUNTERS """)

    @Debug.log_class_func
    def incrementCountRecvMsgBad(self):
        """
        Incrémente le nombre de messages reçus mauvais
        """
        self.ex.execute(""" UPDATE T_COUNTERS set RecvMsgNbBad = RecvMsgNbBad + 1 """)

    @Debug.log_class_func
    def notifyUnsupportedLineTagReceived(self, message):
        """
        Place dans le journal de debug la ligne inconnue
        """
        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = %s,
            DbgContext = 'Bad line tag',
            DbgTs = NOW() """,
            message
        )

    @Debug.log_class_func
    def notifyBadLineReceived(self, message):
        """
        Place dans le journal de debug la ligne reçue malformée
        """
        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = %s,
            DbgContext = 'Bad line',
            DbgTs = NOW() """,
            message
        )

    @Debug.log_class_func
    def incrementCountRecvMsgDataLineNbTotal(self, cpt):
        """
        Incrémente le nombre de lignes traitées (bonnes ou mauvaises)
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbTotal = RecvMsgDataLineNbTotal + %s """, cpt)

    @Debug.log_class_func
    def incrementCountRecvMsgDataLineNbOk(self, cpt):
        """
        Incrémente le nombre de lignes correctes
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbOK = RecvMsgDataLineNbOK + %s """, cpt)

    @Debug.log_class_func
    def incrementCountRecvMsgDataLineNbUnsupported(self, cpt):
        """
        Incrémente le nombre de lignes non reconnues
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbUnsupp = RecvMsgDataLineNbUnsupp + %s """, cpt)

    @Debug.log_class_func
    def incrementCountRecvMsgDataLineNbBad(self, cpt):
        """
        Incrémente le nombre de lignes incorrectes
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbBad = RecvMsgDataLineNbBad + %s """, cpt)

    @Debug.log_class_func
    def updateTeleinfoInst(self, tags):
        """
        Mise à jour du jeu des valeurs téléinfo instantanées
        """
        self.ex.execute(
            """ UPDATE T_TELEINFO_INST set
            PTEC = '{PTEC}',
            PAPP = {PAPP},
            IINST = {IINST},
            HC = {HCHC},
            HP = {HCHP},
            ADCO = {ADCO},
            ISOUSC = {ISOUSC},
            IMAX = {IMAX},
            OPTARIF = '{OPTARIF}',
            HHPHC = '{HHPHC}',
            ETAT = {MOTDETAT},
            TS = '{TS}' """.format_map(tags)
        )

    @Debug.log_class_func
    def updateTeleinfoHisto(self, tags):
        """
        Insertion d'une nouvelle valeur téléinfo instantanée dans l'historique
        """
        self.ex.execute(
            """ INSERT T_HISTO set 
            PTEC = '{PTEC}',
            PAPP = {PAPP},
            IINST = {IINST},
            HC = {HCHC},
            HP = {HCHP},
            ETAT = {MOTDETAT},
            TEMP = {TEMPERATURE},
            RH = {RH},
            PA = {PRESSION_ATMOS},
            TS = '{TS}' on duplicate key UPDATE TS = 'TS' """.format_map(tags)
        )

    @Debug.log_class_func
    def incrementCountEnvRelativeHumidityNbReadTotal(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvRelativeHumidityNbReadTotal = EnvRelativeHumidityNbReadTotal + 1 """)

    @Debug.log_class_func
    def incrementCountEnvRelativeHumidityNbReadOk(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement qui sont un succès
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvRelativeHumidityNbReadOk = EnvRelativeHumidityNbReadOk + 1 """)

    @Debug.log_class_func
    def incrementCountEnvRelativeHumidityNbReadFailed(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement qui sont en échec
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvRelativeHumidityNbReadFailed = EnvRelativeHumidityNbReadFailed + 1 """)

    @Debug.log_class_func
    def incrementCountEnvRelativeHumidityNbReadInvalid(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement qui sont hors des bornes acceptables
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvRelativeHumidityNbReadInvalid = EnvRelativeHumidityNbReadInvalid + 1 """)

    @Debug.log_class_func
    def setCountEnvRelativeHumidityReadLastTs(self, ts):
        """
        Renseigne le moment de la dernière lecture des données de l'environnement
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvRelativeHumidityReadLastTs = %s """, ts)

    @Debug.log_class_func
    def incrementCountEnvTemperatureNbReadTotal(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvTemperatureNbReadTotal = EnvTemperatureNbReadTotal + 1 """)

    @Debug.log_class_func
    def incrementCountEnvTemperatureNbReadOk(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement qui sont un succès
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvTemperatureNbReadOk = EnvTemperatureNbReadOk + 1 """)

    @Debug.log_class_func
    def incrementCountEnvTemperatureNbReadFailed(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement qui sont en échec
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvTemperatureNbReadFailed = EnvTemperatureNbReadFailed + 1 """)

    @Debug.log_class_func
    def incrementCountEnvTemperatureNbReadInvalid(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement qui sont hors des bornes acceptables
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvTemperatureNbReadInvalid = EnvTemperatureNbReadInvalid + 1 """)

    @Debug.log_class_func
    def setCountEnvTemperatureReadLastTs(self, ts):
        """
        Renseigne le moment de la dernière lecture des données de l'environnement
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvTemperatureReadLastTs = %s """, ts)

    @Debug.log_class_func
    def incrementCountEnvAirPressureNbReadTotal(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvAirPressureNbReadTotal = EnvAirPressureNbReadTotal + 1 """)

    @Debug.log_class_func
    def incrementCountEnvAirPressureNbReadOk(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement qui sont un succès
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvAirPressureNbReadOk = EnvAirPressureNbReadOk + 1 """)

    @Debug.log_class_func
    def incrementCountEnvAirPressureNbReadFailed(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement qui sont en échec
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvAirPressureNbReadFailed = EnvAirPressureNbReadFailed + 1 """)

    @Debug.log_class_func
    def incrementCountEnvAirPressureNbReadInvalid(self):
        """
        Incrémente le nombre total de lectures des données de l'environnement qui sont hors des bornes acceptables
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvAirPressureNbReadInvalid = EnvAirPressureNbReadInvalid + 1 """)

    @Debug.log_class_func
    def setCountEnvAirPressureReadLastTs(self, ts):
        """
        Renseigne le moment de la dernière lecture des données de l'environnement
        """
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvAirPressureReadLastTs = %s """, ts)

    @Debug.log_class_func
    def getDatabaseHistoRowNb(self):
        """
        Requête la BDD sur son occupation
        """
        return self.ex.execute_request_for_simple_value(""" select count(*) from T_HISTO """)

    @Debug.log_class_func
    def getDatabaseHistoTablespace(self):
        """
        Requête la BDD sur son occupation
        """
        return self.ex.execute_request_for_simple_value(
            """ SELECT round(((data_length + index_length) / 1024 / 1024), 2) FROM information_schema.TABLES
                WHERE table_schema = 'D_TELEINFO' AND table_name = 'T_HISTO' """)

    @Debug.log_class_func
    def getDatabaseGlobalHeapMax(self):
        """
        Requête la BDD sur son occupation
        """
        return self.ex.execute_request_for_simple_value(
            """ select round(((@@max_heap_table_size) / 1024 / 1024), 2) """)

    @Debug.log_class_func
    def updateRhInst(self, val, ts):
        """
        Mise à jour de la valeur d'humidité instantanée
        """
        self.ex.execute(
            """ UPDATE T_RH_INST set RH = {:f}, TS = '{:s}' """.format(round(val), str(ts)))

    @Debug.log_class_func
    def updateTempInst(self, val, ts):
        """
        Mise à jour de la valeur de température instantanée
        """
        self.ex.execute(
            """ UPDATE T_TEMP_INST set TEMP = {:f}, TS = '{:s}' """.format(val, str(ts)))

    @Debug.log_class_func
    def updatePaInst(self, val, ts):
        """
        Mise à jour de la valeur de pression atmosphérique instantanée
        """
        self.ex.execute(
            """ UPDATE T_PA_INST set PA = {:f}, TS = '{:s}' """.format(val, str(ts)))
