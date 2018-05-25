# -*- coding: UTF-8 -*-

# Dépendances
import MySQLdb  # Besoin de "mysqlclient"
import threading
import Debug  # Besoin de mon décorateur "call_log"
import DatabaseEngine

# *** Notes sur "mysqlclient" ***
# Nécessite sur le système : python3, python3-pip, python3-dev et libmysqlclient-dev
# Nécessite dans python : mysqlclient
# python -m pip install --upgrade pip
# python -m pip install mysqlclient

# *** Configuration de l'utilisateur sous MySQL ***
# create user teleinfo ;
# alter user teleinfo identified by "ti" ;
# create database D_TELEINFO ;
# grant all on D_TELEINFO.* to teleinfo ;

file = __file__.split('\\')[-1]


class SafeRequestExecutor:
    @Debug.call_log
    def __init__(self, pool=None):
        self.connection = MySQLdb.connect('localhost', 'teleinfo', 'ti', 'D_TELEINFO')
        self.engine = self.connection.cursor()
        self.mutex = threading.RLock()

        if pool is not None:
            self.pool = pool
        else:
            self.pool = DatabaseEngine.SqlPool(self)

        self.pool.notifyDatabaseConnected(file)

    @Debug.call_log
    def execute(self, sql, v=None):
        sql = ' '.join(sql.split())
        print("Execute: <" + sql + ">", "(", v, ")")
        self.mutex.acquire()

        if v is None:
            print("(Pas d'argument à la requête)")
            self.engine.execute(sql)
        else:
            if type(v) == list:
                print("(La requête a des arguments, c'est une liste)")
                a = v
            else:
                print("(La requête a des arguments, ce n'est pas une liste)")
                a = [v]

            self.engine.execute(sql, a)

        self.mutex.release()

    @Debug.call_log
    def close(self):

        # Indication de sortie dans la BDD
        self.pool.notifyDatabaseClosing(file)
        self.connection.close()

    @Debug.call_log
    def __enter__(self):
        print("...")

    @Debug.call_log
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.free()

    @Debug.call_log
    def __del__(self):
        print('...')
