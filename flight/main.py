# -*- coding: utf-8 -*-
"""
@author: Cédric Berteletti
"""

import logging
import services.settings as settings


def main(args):
    print("Hello World!")


settings.init()
logging.basicConfig(format="%(asctime)s %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S", level=logging.getLevelName(settings.get("logging.level")))
logging.info("Main flight program started")
if __name__ == "__main__":
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass