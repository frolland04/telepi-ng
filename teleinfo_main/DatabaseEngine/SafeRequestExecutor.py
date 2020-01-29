# -*- coding: UTF-8 -*-

# Dépendances
import mysql.connector as db  # Nécessite sur le système : python3, python3-mysql.connector
import threading

# Sous-modules
import Debug  # Besoin de mon décorateur "log_class_func"
import DatabaseEngine

# Pour le débogage
this_file = __file__.split('\\')[-1]


class SafeRequestExecutor:
    """
    Cette classe implémente un exécuteur mono-connexion de requêtes à la BDD,
    qui peut être utilisé en multithread, garantissant une seule requête à la fois.
    Utilise le pool de requêtes prédéfinies pour ses propres notifications.
    """

    USER_NAME = 'teleinfo'
    USER_PASSWORD = 'ti'
    DATABASE_NAME = 'D_TELEINFO'

    @Debug.log_class_func
    def __init__(self, pool=None):
        """
        Initialisation du 'SafeRequestExecutor' : connection et verrou
        """
        print(this_file + ':', 'DATABASE_NAME=' + self.DATABASE_NAME)

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

        self.pool.notifyDatabaseConnected(this_file)

    @Debug.log_class_func
    def __del__(self):
        """
        Nettoyage du 'SafeRequestExecutor'
        """
        print('...')

    @Debug.log_class_func
    def close(self):
        """
        Fin propre du 'SafeRequestExecutor' : notification au journal et fermeture BDD
        """
        # Indication de sortie dans la BDD
        self.pool.notifyDatabaseClosing(this_file)
        self.connection.close()

    @Debug.log_class_func
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

    @Debug.log_class_func
    def execute_request_for_simple_value(self, sql):
        """
        Exécute une requête avec résultat simple, et le retourne
        """
        with self.mutex:
            try:
                self.engine.execute(sql)
                s = self.engine.fetchall()
                return s[0][0]

            except Exception as e:
                print('Unable to fetch data !', e)
                return ''

    @Debug.log_class_func
    def __enter__(self):
        """
        Entrée de zone, pour gestion de contextes
        """
        print("...")

    @Debug.log_class_func
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Sortie de zone, pour gestion de contextes
        """
        print("...")
