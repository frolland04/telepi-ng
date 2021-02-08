# -*- coding: UTF-8 -*-

# Quelques informations
__author__ = 'Frédéric ROLLAND'
__version__ = '1'

# Importation des sous-modules du module
from DatabaseEngine.SafeRequestExecutor import *
from DatabaseEngine.SqlPool import *

# On affiche simplement le nom du module, au moment de son chargement
print('[' + __name__ + ']', 'author=\'' + __author__ + '\'', 'version=' + __version__)
