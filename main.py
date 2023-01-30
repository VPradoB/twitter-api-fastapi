import os

from fastapi import FastAPI

app = FastAPI()


# This  is used to load all the routers from the src folder
for filename in os.listdir('src'):
    if filename != '__pycache__' and filename != 'shared':
        app.include_router(
            __import__(f'src.{filename}.infrastructure.router',
                       fromlist=['router']).router,
            prefix=f'/{filename}'
        )
