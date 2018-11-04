# -*- coding: UTF-8 -*-

# Dépendances
# ...

file = __file__.split('\\')[-1]


def call_log(method):
    """Ceci est un décorateur de méthode pour afficher automatiquement un message à l'appel de cette méthode"""
    def print_identification(*args, **kwargs):
        id = {
            '__init__': 'Initialisation',
            '__del__': 'Nettoyage',
            '__enter__': 'Entrée de zone',
            '__exit__': 'Sortie de zone',
            'close': 'Libération'
        }

        # Note: 'args' est un tuple qui contient les arguments, pour une méthode de classe c'est 'self'.
        methodName = method.__name__
        className = args[0].__class__.__name__

        # Si c'est une méthode spéciale on traduit le nom sinon on affiche le nom réel de la méthode
        if methodName in id:
            identName = id[methodName]
        else:
            identName = 'Appel de ' + methodName + '()'

        print("Debug: %s de '%s'" % (identName, className))
        return method(*args, **kwargs)

    return print_identification


def log_except(e, msg):
    """Petite fonction gentille pour afficher les caractéristiques d'une exception"""
    print('\n>>> EXCEPTION :\n', e, '(', msg, ')\n')
