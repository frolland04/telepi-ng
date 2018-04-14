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

    def notifyDatabaseConnected(self, context=''):
        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = 'DATABASE CONNECTED',
            DbgContext = %s,
            DbgTs = NOW() """,
            context
        )

    def notifyDatabaseClosing(self, context=''):
        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = 'DATABASE IS CLOSING',
            DbgContext = %s,
            DbgTs = NOW() """,
            context
        )

    def notifySystemFatalCondition(self, context=''):
        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = 'FATAL EXCEPTION CAUSED ABORTING',
            DbgContext = %s,
            DbgTs = NOW() """,
            context
        )

    def incrementCountRecvMsg(self, ts=0):
        """Incrémente le nombre de messages reçus (bons ou mauvais)
        et horodatage du dernier message reçu"""

        self.ex.execute(
            """ UPDATE T_COUNTERS set
            RecvMsgNbTotal = RecvMsgNbTotal + 1,
            RecvMsgLastTs = %s """,
            ts
        )

    def incrementCountRecvMsgOk(self):
        """Incrémente le nombre de messages reçus bons"""
        self.ex.execute(""" UPDATE T_COUNTERS set RecvMsgNbOK = RecvMsgNbOK + 1 """)

    def incrementCountRecvMsgBad(self):
        """Incrémente le nombre de messages reçus mauvais"""
        self.ex.execute(""" UPDATE T_COUNTERS set RecvMsgNbBad = RecvMsgNbBad + 1 """)

    def notifyUnsupportedLineTagReceived(self, message):
        """Place dans le journal de debug la ligne inconnue"""

        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = %s,
            DbgContext = 'Bad line tag',
            DbgTs = NOW() """,
            message
        )

    def notifyBadLineReceived(self, message):
        """Place dans le journal de debug la ligne reçue malformée"""

        self.ex.execute(
            """ INSERT T_DBG_ENTRIES set
            DbgMessage = %s,
            DbgContext = 'Bad line',
            DbgTs = NOW() """,
            message
        )

    def incrementCountRecvMsgDataLineNbTotal(self, cpt):
        """Incrémente le nombre de lignes traitées (bonnes ou mauvaises)"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbTotal = RecvMsgDataLineNbTotal + %s """, cpt)

    def incrementCountRecvMsgDataLineNbOk(self, cpt):
        """Incrémente le nombre de lignes correctes"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbOK = RecvMsgDataLineNbOK + %s """, cpt)

    def incrementCountRecvMsgDataLineNbUnsupported(self, cpt):
        """Incrémente le nombre de lignes non reconnues"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbUnsupp = RecvMsgDataLineNbUnsupp + %s """, cpt)

    def incrementCountRecvMsgDataLineNbBad(self, cpt):
        """Incrémente le nombre de lignes incorrectes"""
        self.ex.execute(
            """ UPDATE T_COUNTERS set RecvMsgDataLineNbBad = RecvMsgDataLineNbBad + %s """, cpt)

    def updateTeleinfoInst(self, tags):
        """Mise à jour du jeu des valeurs téléinfo instantanées"""

        self.ex.execute(
            """ UPDATE T_TELEINFO_INST set
            PTEC = %(PTEC)s,
            PAPP = %(PAPP)s,
            IINST = %(IINST)s,
            HC = %(HCHC)s,
            HP = %(HCHP)s,
            ADCO = %(ADCO)s,
            ISOUSC = %(ISOUSC)s,
            IMAX = %(IMAX)s,
            OPTARIF = %(OPTARIF)s,
            HHPHC = %(HHPHC)s,
            ETAT = %(MOTDETAT)s,
            TEMPERATURE = %(TEMPERATURE)s,
            RH = %(RH)s,
            TS = %(TS)s """,
            tags
        )

    def updateTeleinfoHisto(self, tags):
        """Insertion d'une nouvelle valeur téléinfo instantanée dans l'historique"""

        self.ex.execute(
            """ INSERT T_TELEINFO_HISTO set 
            PTEC = %(PTEC)s,
            PAPP = %(PAPP)s,
            IINST = %(IINST)s,
            HC = %(HCHC)s,
            HP = %(HCHP)s,
            ADCO = %(ADCO)s,
            ISOUSC = %(ISOUSC)s,
            IMAX = %(IMAX)s,
            OPTARIF = %(OPTARIF)s,
            HHPHC = %(HHPHC)s,
            ETAT = %(MOTDETAT)s,
            TEMPERATURE = %(TEMPERATURE)s,
            RH = %(RH)s,
            TS = %(TS)s on duplicate key UPDATE TS = TS""",
            tags
        )
