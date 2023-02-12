import os
from src.shared.infrastructure.logger import configure_logger
from fastapi import FastAPI

app = FastAPI()
configure_logger(
    logger_name=os.getenv('LOGGER_NAME'),
    logger_host=os.getenv('LOGGER_HOST'),
    logger_port=int(os.getenv('LOGGER_PORT'))
)

# This  is used to load all the routers from the src folder
for filename in os.listdir('src'):
    if filename != '__pycache__' and filename != 'shared':
        app.include_router(
            __import__(f'src.{filename}.infrastructure.router',
                       fromlist=['router']).router,
            prefix=f'/{filename}'
        )
