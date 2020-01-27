# -*- coding: UTF-8 -*-

# Dépendances
import mysql.connector as db
import threading

import Debug  # Besoin de mon décorateur "call_log"
import DatabaseEngine

# *** Notes sur "mysql.connector" ***
# Nécessite sur le système : python3, python3-mysql.connector

# *** Configuration de l'utilisateur sous MySQL ***
# CREATE USER `teleinfo` ;
# ALTER USER `teleinfo` IDENTIFIED BY "ti" ;
# CREATE DATABASE `D_TELEINFO` ;
# GRANT ALL ON `D_TELEINFO`.`*` TO `teleinfo` ;

file = __file__.split('\\')[-1]


class SafeRequestExecutor:
    USER_NAME = 'teleinfo'
    USER_PASSWORD = 'ti'
    DATABASE_NAME = 'D_TELEINFO'

    @Debug.call_log
    def __init__(self, pool=None):
        print(file + ':', 'DATABASE_NAME=' + self.DATABASE_NAME)

        self.connection = db.connect(host='localhost',
                                     user=self.USER_NAME,
                                     password=self.USER_PASSWORD,
                                     database=self.DATABASE_NAME)
        self.engine = self.connection.cursor()
        self.mutex = threading.RLock()

        if pool is not None:
            self.pool = pool
        else:
            self.pool = DatabaseEngine.SqlPool(self)

        self.pool.notifyDatabaseConnected(file)

    @Debug.call_log
    def execute(self, sql, v=None):
        """
        Exécution d'une requête sur le moteur de base de données, avec garantie qu'une seule s'exécute à la fois
        """
        # Se débrouille tout seul avec .acquire() and .release()
        # en entrée et sortie du bloc, même sur exception
        with self.mutex:
            sql = ' '.join(sql.split())
            print("Execute: <" + sql + ">", "(", v, ")")

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

    @Debug.call_log
    def execute_request_for_simple_value(self, sql):
        with self.mutex:
            try:
                self.engine.execute(sql)
                s = self.engine.fetchall()
                return s[0][0]

            except Exception as e:
                print('Unable to fetch data !', e)
                return ''

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
