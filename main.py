import glob
import importlib
import os
from dotenv import load_dotenv

import uvicorn

from src.shared.infrastructure.logs import configure_logger
from src.shared.infrastructure.database import Database
from fastapi import FastAPI

load_dotenv()
app = FastAPI()

# the logger is configured here
configure_logger(
    logger_name=os.getenv('LOGGER_NAME'),
    logger_host=os.getenv('LOGGER_HOST'),
    logger_port=int(os.getenv('LOGGER_PORT'))
)

Database.create_database_sqlite(
    database_url=f'sqlite:///{os.getenv("DATABASE_URL")}'
    )


# This  is used to load all the routers from the src folder
def include_routers(app: FastAPI):
    path = 'src/*/infrastructure/router.py'
    for filename in glob.glob(path):
        module = filename.replace('/', '.').replace('\\', '.')[:-3]
        router = importlib.import_module(module)
        app.include_router(router.router, prefix=f'/{module.split(".")[1]}')


include_routers(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)