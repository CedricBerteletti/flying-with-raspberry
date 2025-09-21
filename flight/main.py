# -*- coding: utf-8 -*-
"""
@author: Cédric Berteletti
"""

import logging
import uvicorn
from fastapi import FastAPI
import services.settings as settings
from controllers.hello_controller import app as hello_router

app = FastAPI(title="Flying Raspberry API")

# Mount the API router
app.mount("/hello", hello_router)

def main(args):
    # Initialize settings and logging
    settings.init()
    logging.basicConfig(format="%(asctime)s %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S", level=logging.getLevelName(settings.get("logging.level")))
    logging.info("Main flight program started")
    
    # Start the FastAPI server
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        logging.info("Server stopped")