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
            TEMPERATURE = {TEMPERATURE},
            RH = {RH},
            TS = '{TS}' """.format_map(tags)
        )

    @Debug.call_log
    def updateTeleinfoHisto(self, tags):
        """Insertion d'une nouvelle valeur téléinfo instantanée dans l'historique"""

        self.ex.execute(
            """ INSERT T_TELEINFO_HISTO set 
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
            TEMPERATURE = {TEMPERATURE},
            RH = {RH},
            TS = '{TS}' on duplicate key UPDATE TS = TS""".format_map(tags)
        )
