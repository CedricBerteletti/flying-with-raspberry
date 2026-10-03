# -*- coding: utf-8 -*-
"""
@author: Cédric Berteletti
Pour charger les fichiers de configuration
"""

import configparser


def init():
    """Initialise la configuration depuis le fichier de paramètres."""
    global config
    config = configparser.ConfigParser(inline_comment_prefixes="#")
    config.read("flight.ini")


def get(cle):
    """Récupère une valeur de configuration dans la section par défaut."""
    global config
    return config.get("DEFAULT", cle)


def get_bool(cle):
    """Récupère une valeur booléenne de configuration."""
    global config
    return config.getboolean("DEFAULT", cle)


def get_int(cle):
    """Récupère une valeur entière de configuration."""
    global config
    return config.getint("DEFAULT", cle)