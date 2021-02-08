# -*- coding: UTF-8 -*-

# Pour le débogage
this_file = __file__.split('\\')[-1]


def log_class_func(f):
    """
    Ceci est un décorateur de méthode pour afficher automatiquement un message à l'appel de cette méthode
    """

    def log(*args, **kwargs):
        """
        Cette fonction embarquée affiche le texte souhaité et appelle la fonction décorée
        """
        translations = {
            # '__init__': '[I]',
            # '__del__': '[D]',
            # '__enter__': '[E]',
            # '__exit__': '[X]',
            # 'close': '[C]'
        }

        # Note: 'args' est un tuple qui contient les arguments, pour une méthode de classe le premier c'est 'self'.
        # On y trouve alors dedans le nom de la classe.
        method_name = f.__name__
        class_name = args[0].__class__.__name__

        # Si c'est une méthode spéciale on traduit le nom sinon on affiche le nom réel de la méthode
        if method_name in translations:
            method_msg = translations[method_name]
        else:
            method_msg = 'Appel de ' + method_name + '()'

        print("Debug: %s de '%s'" % (method_msg, class_name))
        return f(*args, **kwargs)

    return log


def log_func(f):
    """
    Ceci est un décorateur de fonction pour afficher automatiquement un message à l'appel de cette fonction
    """

    def log(*args, **kwargs):
        """
        Cette fonction embarquée affiche le texte souhaité et appelle la fonction décorée
        """
        print("Debug: Appel de " + f.__name__ + '()')
        return f(*args, **kwargs)

    return log


def log_exc(e, msg):
    """
    Petite fonction gentille pour afficher les caractéristiques d'une exception
    """
    print('\n>>> EXCEPTION :\n', e, '(', msg, ')\n')
