# -*- coding: UTF-8 -*-

# Dépendances
import Debug  # Besoin de mon décorateur 'call_log'
import DatabaseEngine


file = __file__.split('\\')[-1]


class SqlPool:
    @Debug.call_log
    def __init__(self, ex=None):
        if ex is not None:
            self.ex = ex
        else:
            self.ex = DatabaseEngine.SafeRequestExecutor(self)

    @Debug.call_log
    def close(self):
        print('...')

    @Debug.call_log
    def __enter__(self):
        print('...')

    @Debug.call_log
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @Debug.call_log
    def __del__(self):
        print('...')

    @Debug.call_log
    def notifyDatabaseConnected(self, context=''):
        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = 'DATABASE CONNECTED',
            DbgContext = %s,
            DbgTs = NOW() """,
            context
        )

    @Debug.call_log
    def notifyDatabaseClosing(self, context=''):
        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = 'DATABASE IS CLOSING',
            DbgContext = %s,
            DbgTs = NOW() """,
            context
        )

    @Debug.call_log
    def notifySystemFatalCondition(self, context=''):
        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = 'FATAL EXCEPTION CAUSED ABORTING',
            DbgContext = %s,
            DbgTs = NOW() """,
            context
        )

    @Debug.call_log
    def incrementCountRecvMsg(self, ts=0):
        """Incrémente le nombre de messages reçus (bons ou mauvais)
        et horodatage du dernier message reçu"""

        self.ex.execute(
            """ UPDATE T_COUNTERS set
            RecvMsgNbTotal = RecvMsgNbTotal + 1,
            RecvMsgLastTs = %s """,
            ts
        )

    @Debug.call_log
    def incrementCountRecvMsgOk(self):
        """Incrémente le nombre de messages reçus bons"""
        self.ex.execute(""" UPDATE T_COUNTERS set RecvMsgNbOK = RecvMsgNbOK + 1 """)

    @Debug.call_log
    def getCountRecvMsgOk(self):
        """Récupère le nombre de messages reçus bons"""
        return self.ex.execute_request_for_simple_value(""" SELECT RecvMsgNbOK FROM T_COUNTERS """)

    @Debug.call_log
    def incrementCountRecvMsgBad(self):
        """Incrémente le nombre de messages reçus mauvais"""
        self.ex.execute(""" UPDATE T_COUNTERS set RecvMsgNbBad = RecvMsgNbBad + 1 """)

    @Debug.call_log
    def notifyUnsupportedLineTagReceived(self, message):
        """Place dans le journal de debug la ligne inconnue"""

        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = %s,
            DbgContext = 'Bad line tag',
            DbgTs = NOW() """,
            message
        )

    @Debug.call_log
    def notifyBadLineReceived(self, message):
        """Place dans le journal de debug la ligne reçue malformée"""

        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = %s,
            DbgContext = 'Bad line',
            DbgTs = NOW() """,
            message
        )

    @Debug.call_log
    def incrementCountRecvMsgDataLineNbTotal(self, cpt):
        """Incrémente le nombre de lignes traitées (bonnes ou mauvaises)"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbTotal = RecvMsgDataLineNbTotal + %s """, cpt)

    @Debug.call_log
    def incrementCountRecvMsgDataLineNbOk(self, cpt):
        """Incrémente le nombre de lignes correctes"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbOK = RecvMsgDataLineNbOK + %s """, cpt)

    @Debug.call_log
    def incrementCountRecvMsgDataLineNbUnsupported(self, cpt):
        """Incrémente le nombre de lignes non reconnues"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbUnsupp = RecvMsgDataLineNbUnsupp + %s """, cpt)

    @Debug.call_log
    def incrementCountRecvMsgDataLineNbBad(self, cpt):
        """Incrémente le nombre de lignes incorrectes"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbBad = RecvMsgDataLineNbBad + %s """, cpt)

    @Debug.call_log
    def updateTeleinfoInst(self, tags):
        """Mise à jour du jeu des valeurs téléinfo instantanées"""

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

    @Debug.call_log
    def updateTeleinfoHisto(self, tags):
        """Insertion d'une nouvelle valeur téléinfo instantanée dans l'historique"""

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

    @Debug.call_log
    def incrementCountEnvRelativeHumidityNbReadTotal(self):
        """Incrémente le nombre total de lectures des données de l'environnement"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvRelativeHumidityNbReadTotal = EnvRelativeHumidityNbReadTotal + 1 """)

    @Debug.call_log
    def incrementCountEnvRelativeHumidityNbReadOk(self):
        """Incrémente le nombre total de lectures des données de l'environnement qui sont un succès"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvRelativeHumidityNbReadOk = EnvRelativeHumidityNbReadOk + 1 """)

    @Debug.call_log
    def incrementCountEnvRelativeHumidityNbReadFailed(self):
        """Incrémente le nombre total de lectures des données de l'environnement qui sont en échec"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvRelativeHumidityNbReadFailed = EnvRelativeHumidityNbReadFailed + 1 """)

    @Debug.call_log
    def incrementCountEnvRelativeHumidityNbReadInvalid(self):
        """Incrémente le nombre total de lectures des données de l'environnement qui sont hors des bornes acceptables"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvRelativeHumidityNbReadInvalid = EnvRelativeHumidityNbReadInvalid + 1 """)

    @Debug.call_log
    def setCountEnvRelativeHumidityReadLastTs(self, ts):
        """Renseigne le moment de la dernière lecture des données de l'environnement"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvRelativeHumidityReadLastTs = %s """, ts)

    @Debug.call_log
    def incrementCountEnvTemperatureNbReadTotal(self):
        """Incrémente le nombre total de lectures des données de l'environnement"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvTemperatureNbReadTotal = EnvTemperatureNbReadTotal + 1 """)

    @Debug.call_log
    def incrementCountEnvTemperatureNbReadOk(self):
        """Incrémente le nombre total de lectures des données de l'environnement qui sont un succès"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvTemperatureNbReadOk = EnvTemperatureNbReadOk + 1 """)

    @Debug.call_log
    def incrementCountEnvTemperatureNbReadFailed(self):
        """Incrémente le nombre total de lectures des données de l'environnement qui sont en échec"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvTemperatureNbReadFailed = EnvTemperatureNbReadFailed + 1 """)

    @Debug.call_log
    def incrementCountEnvTemperatureNbReadInvalid(self):
        """Incrémente le nombre total de lectures des données de l'environnement qui sont hors des bornes acceptables"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvTemperatureNbReadInvalid = EnvTemperatureNbReadInvalid + 1 """)

    @Debug.call_log
    def setCountEnvTemperatureReadLastTs(self, ts):
        """Renseigne le moment de la dernière lecture des données de l'environnement"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvTemperatureReadLastTs = %s """, ts)

    @Debug.call_log
    def incrementCountEnvAirPressureNbReadTotal(self):
        """Incrémente le nombre total de lectures des données de l'environnement"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvAirPressureNbReadTotal = EnvAirPressureNbReadTotal + 1 """)

    @Debug.call_log
    def incrementCountEnvAirPressureNbReadOk(self):
        """Incrémente le nombre total de lectures des données de l'environnement qui sont un succès"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvAirPressureNbReadOk = EnvAirPressureNbReadOk + 1 """)

    @Debug.call_log
    def incrementCountEnvAirPressureNbReadFailed(self):
        """Incrémente le nombre total de lectures des données de l'environnement qui sont en échec"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvAirPressureNbReadFailed = EnvAirPressureNbReadFailed + 1 """)

    @Debug.call_log
    def incrementCountEnvAirPressureNbReadInvalid(self):
        """Incrémente le nombre total de lectures des données de l'environnement qui sont hors des bornes acceptables"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvAirPressureNbReadInvalid = EnvAirPressureNbReadInvalid + 1 """)

    @Debug.call_log
    def setCountEnvAirPressureReadLastTs(self, ts):
        """Renseigne le moment de la dernière lecture des données de l'environnement"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set EnvAirPressureReadLastTs = %s """, ts)

    @Debug.call_log
    def getDatabaseHistoRowNb(self):
        """Requête la BDD sur son occupation"""
        return self.ex.execute_request_for_simple_value(""" select count(*) from T_HISTO """)

    @Debug.call_log
    def getDatabaseHistoTablespace(self):
        """Requête la BDD sur son occupation"""
        return self.ex.execute_request_for_simple_value(""" SELECT round(((data_length + index_length) / 1024 / 1024), 2) FROM information_schema.TABLES
         WHERE table_schema = 'D_TELEINFO' AND table_name = 'T_HISTO'""")

    @Debug.call_log
    def getDatabaseGlobalHeapMax(self):
        """Requête la BDD sur son occupation"""
        return self.ex.execute_request_for_simple_value(""" select round(((@@max_heap_table_size) / 1024 / 1024), 2) """)
