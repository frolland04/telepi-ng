# -*- coding: UTF-8 -*-

# Dépendances
import serial  # Besoin de 'apt-get install python-serial' ou 'python -m pip install pyserial'
import datetime
import threading
import time

# Sous-modules
import Debug  # Besoin de mon décorateur 'call_log'

file = __file__.split('\\')[-1]


class MessageProcessor(threading.Thread):
    """
    Classe de collecte TéléInformation ERDF par le port série.
    Fonctionne en continu, décode les messages, peuple les valeurs et valide ou pas la mesure.
    """

    # Port série utilisé
    MESSAGE_PORT_NAME = '/dev/ttyAMA0'

    @Debug.call_log
    def __init__(self, ex):
        # Ouverture du port série
        print(file + ':', 'MESSAGE_PORT_NAME=' + self.MESSAGE_PORT_NAME)

        self.si = serial.Serial(
            port=self.MESSAGE_PORT_NAME,
            baudrate=1200,
            parity=serial.PARITY_EVEN,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.SEVENBITS
        )

        self.si.flushInput()

        # Handle pour exécuter les requêtes à la BDD
        self.ex = ex

        # Données décodées du dernier message Télé-information ERDF reçu :
        # Dictionnaire des étiquettes connues et la valeur courante associée
        # pour le message en cours de traitement
        # + drapeau pour indiquer si la dernière lecture Télé-information ERDF
        # est valide (et donc représentée par le dictionnaire!)
        self.__tags = \
            {
                'PTEC': '',
                'PAPP': 0,
                'IINST': 0,
                'HCHC': 0,
                'HCHP': 0,
                'ADCO': 0,
                'ISOUSC': 0,
                'IMAX': 0,
                'OPTARIF': '',
                'HHPHC': '',
                'MOTDETAT': '',
                'OK': False
            }

        # On est dans une sous-classe thread dédiée + condition d'arrêt
        threading.Thread.__init__(self)
        self.end = False
        self.start()

    @Debug.call_log
    def close(self):
        """Fin propre : arrêt thread (sur contrôle d'une variable dans le corps de la boucle)"""
        self.end = True
        self.si.close()

    @Debug.call_log
    def run(self):
        """Boucle de réception des messages, exécutée par le thread dédié"""
        while not self.end:
            self.teleinfo_wait_message()

    def teleinfo_wait_message(self):
        """
        Fonction préliminaire au décodage : localise un message entier
        """

        # Attendre le début du message: '0x002' (STX)
        while self.si.read(1)[0] != 0x02:
            pass

        # Lire jusqu'à la fin du message: '0x003' (ETX)
        msg = ''
        fin_msg = False
        while not fin_msg:
            ba = self.si.read(1)
            if ba[0] != 0x03:
                msg = msg + chr(ba[0])
            else:
                fin_msg = True

        ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('DBG_MSG:', '>', msg, '<', ts)

        # Incrémente le nombre de messages reçus (bons ou mauvais)
        # et horodatage du dernier message reçu
        self.ex.pool.incrementCountRecvMsg(ts)

        # Analyse du message courant
        ret = self.teleinfo_read_message(msg, ts)
        if ret:
            # Incrémente le nombre de messages reçus bons
            self.ex.pool.incrementCountRecvMsgOk()
        else:
            # Incrémente le nombre de messages reçus mauvais
            self.ex.pool.incrementCountRecvMsgBad()

    # =========================================================================
    # Calcul du checksum Téléinfo ERDF sur une ligne de message

    def teleinfo_checksum_ligne(self, etiquette, valeur):
        # Somme des codes des caractères jusqu'à la fin de la valeur
        s = 0
        for ca in etiquette:
            s += ord(ca)

        # Espace de séparation entre étiquette et valeur
        s += 0x20

        for ca in valeur:
            s += ord(ca)

        # Recalage pour être le code d'un caractère affichable
        s = (s & 0x3F) + 0x20

        print("Le checksum devrait être '", chr(s), "' qui est le code 0x", s)
        return chr(s)

    # =========================================================================
    # Analyse de la valeur d'une étiquette portée par une ligne de message

    def teleinfo_read_ligne(self, etiquette, valeur, dictionnaire):
        """
        Si l'étiquette est connue, répercute la valeur dans le dictionnaire
        """

        if etiquette in dictionnaire:
            if etiquette == 'PTEC' or etiquette == 'OPTARIF':
                #  Pour les étiquettes 'PTEC' et 'OPTARIF', j'ai choisi de tronquer la valeur aux 2 premiers caractères
                dictionnaire[etiquette] = valeur[0:2]
            else:
                # Pour les autres on met la valeur telle que reçue
                dictionnaire[etiquette] = valeur

            print("Nouvelle valeur de", etiquette, "=", dictionnaire[etiquette])

    # =========================================================================
    # Lecture et analyse d'un message Téléinfo ERDF

    def teleinfo_read_message(self, message, ts):
        """
        Fonction principale du décodage : analyse ligne par ligne
        """

        # Maintenant qu'on a un message entier, découpons-le, mettons chaque ligne dans un tableau
        lignes = [
            ligne.split(" ")
            for ligne in message.strip("\r\n\x03").split("\r\n")
        ]

        # On obtient un certain nombre de lignes
        nb_lignes = len(lignes)
        print('>>> lignes: ' + repr(nb_lignes))

        # Boucle de parcours des lignes avec cpt des lignes valides ou non
        i = 0
        cpt_good = 0
        cpt_badline = 0
        cpt_badtag = 0

        while i < nb_lignes:
            # On prend une des lignes
            ligne = lignes[i]
            print("i =", i, ligne)

            is_good = False
            is_badtag = False

            # Contrôle du checksum et récupération des valeurs instantanées
            if len(ligne) >= 2:
                # Au moins 2 éléments : étiquette et valeur
                # -> on calcule le checksum correspondant
                cs = self.teleinfo_checksum_ligne(ligne[0], ligne[1])

                if (cs == " ") and (len(ligne) == 4) and (ligne[2] == "") and (ligne[3] == ""):
                    # Si le checksum est un espace, il a été pris pour un séparateur
                    # -> alors cela a créé 2 chaînes vides supplémentaires dans la ligne, qui compte alors 4 blocs
                    is_good = True
                else:
                    # Si le checksum n'est pas un espace, alors on a bien 3 chaînes au total
                    # -> le checksum fourni doit être celui calculé
                    if (cs != " ") and (len(ligne) == 3) and (cs == ligne[2]):
                        is_good = True

                # Est-ce qu'on connaît cette étiquette ?
                if ligne[0] not in self.__tags:
                    is_badtag = True

            if is_good:
                if is_badtag:
                    print("ligne inconnue")
                    cpt_badtag += 1

                    # Place dans le journal de debug la ligne inconnue
                    dbg = str(ligne)
                    self.ex.pool.notifyUnsupportedLineTagReceived(dbg)

                else:
                    print("ligne OK")
                    cpt_good += 1

                    # Analyse de la ligne et répercussion dans la liste de valeurs
                    self.teleinfo_read_ligne(ligne[0], ligne[1], self.__tags)

            else:
                print("ligne KO")
                cpt_badline += 1

                # Place dans le journal de debug la ligne reçue malformée
                dbg = str(ligne)
                self.ex.pool.notifyBadLineReceived(dbg)

            i += 1

        if i > 0:
            # Incrémente le nombre de lignes traitées (bonnes ou mauvaises)
            self.ex.pool.incrementCountRecvMsgDataLineNbTotal(i)

        if cpt_good > 0:
            # Incrémente le nombre de lignes correctes
            self.ex.pool.incrementCountRecvMsgDataLineNbOk(cpt_good)

        if cpt_badtag > 0:
            # Incrémente le nombre de lignes non reconnues
            self.ex.pool.incrementCountRecvMsgDataLineNbUnsupported(cpt_badtag)

        if cpt_badline > 0:
            # Incrémente le nombre de lignes incorrectes
            self.ex.pool.incrementCountRecvMsgDataLineNbBad(cpt_badline)

        if cpt_good == i:
            print("**** message OK ****")
            ret = True

            # On ajoute la date/heure de collecte aux valeurs du dictionnaire
            self.__tags['TS'] = ts

            # On ajoute l'indicateur de validité
            self.__tags['OK'] = True

            # On montre les tags
            print(self.__tags)

        else:
            print("**** message KO ****")
            ret = False

            # On invalide la collecte
            self.__tags['OK'] = False

        # On retourne l'information sur l'intégrité du message courant : bonne ou mauvaise
        return ret

    @property
    def tags(self):
        """Je suis une @propriété Python."""
        print("MessageProcessor.tags@get")
        return self.__tags

    @Debug.call_log
    def __enter__(self):
        print('...')

    @Debug.call_log
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @Debug.call_log
    def __del__(self):
        print('...')
