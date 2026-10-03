# -*- coding: utf-8 -*-
"""
@author: Cédric Berteletti
"""

import logging
import uvicorn
from fastapi import FastAPI
import services.config as config
from controlleurs.salut_controlleur import app as salut_routeur
from controlleurs.camera_controlleur import app as camera_routeur

app = FastAPI(title="Flying Raspberry API")

# Mount the API routers
app.mount("/api/salut", salut_routeur)
app.mount("/api/camera", camera_routeur)

def main(args):
    # Initialisation des paramètres de configuration et du journal
    config.init()
    logging.basicConfig(format="%(asctime)s %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S", level=logging.getLevelName(config.get("logging.level")))
    logging.info("LANCEMENT DU PROGRAMME DE VOL PRINCIPAL")
    
    # Démarre le serveur FastAPI
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        logging.info("SERVEUR ARRÊTÉ")