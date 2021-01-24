# -*- coding: UTF-8 -*-

"""
Quelques trucs pour faciliter la gestion structurée des erreurs.
"""

# Pour le débogage
this_file = __file__.split('\\')[-1]


class EnterExitLogger:
    """
    Cette classe s'utilise en objet membre pour attacher des fonctions à exécuter à __enter__ et __exit__
    c'est à dire lorsque on entre ou on sort d'une zone de contexte d'exécution (cf. 'with').
    """
    def __init__(self, instance_id=None):
        print('EnterExitLogger', '__init__()', instance_id)
        self.instance_id = instance_id
        self.normal_exit_func = None
        self.normal_exit_arg = None
        self.unexpected_exit_func = None
        self.unexpected_exit_arg = None
        self.unexpected_exit_suppress_exc = True

    def __del__(self):
        print('EnterExitLogger', '__del__()', self.instance_id)

    def register_normal_exit_func(self, func, arg=None):
        self.normal_exit_func = func
        self.normal_exit_arg = arg

    def register_unexpected_exit_func(self, func, arg=None, suppress_exc=True):
        self.unexpected_exit_func = func
        self.unexpected_exit_suppress_exc = suppress_exc
        self.unexpected_exit_arg = arg

    def __enter__(self):
        print('EnterExitLogger', '__enter__()', self.instance_id)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EnterExitLogger', '__exit__()', self.instance_id, exc_type, exc_val, exc_tb)
        # Pas d'exception : sortie normale
        if exc_val is None and self.normal_exit_func is not None:
            if self.normal_exit_arg is not None:
                self.normal_exit_func(self.normal_exit_arg)
            else:
                self.normal_exit_func()
        else:
            # Une exception : sortie inattendue
            if exc_val is not None and self.unexpected_exit_func is not None:
                if self.unexpected_exit_arg is not None:
                    self.unexpected_exit_func(self.unexpected_exit_arg)
                else:
                    self.unexpected_exit_func()

        # Supression (ou pas) de la propagation de l'exception
        return self.unexpected_exit_suppress_exc
