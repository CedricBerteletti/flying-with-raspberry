# -*- coding: utf-8 -*-
"""
@author: Cédric Berteletti
Métaclasse Singleton
"""

from threading import Lock


class SingletonMeta(type):
    """
    Il s'agit d'une implémentation thread-safe du patron Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    Nous avons maintenant un objet de verrou utilisé pour synchroniser les
    threads lors du premier accès au Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Les modifications éventuelles de la valeur de l'argument `__init__`
        n'affectent pas l'instance renvoyée.
        """
        # Imaginez maintenant que le programme vient de démarrer. Comme il n'y
        # a pas encore d'instance Singleton, plusieurs threads peuvent passer
        # simultanément le test précédent et arriver presque au même moment à
        # cet endroit. Le premier d'entre eux acquiert le verrou et continue,
        # tandis que les autres attendent ici.
        with cls._lock:
            # Le premier thread à acquérir le verrou passe dans cette condition,
            # crée l'instance Singleton et quitte ensuite le bloc de verrouillage.
            # Un autre thread, qui attendait la libération du verrou, peut alors
            # entrer dans cette section. Mais comme le champ Singleton est déjà
            # initialisé, il ne créera pas un nouvel objet.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]