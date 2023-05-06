import os
import json
try:
    # link: https://fastapi.tiangolo.com/
    # pip install fastapi
    from pydantic import BaseModel
    from fastapi import FastAPI, status
    from fastapi.exceptions import HTTPException

except ModuleNotFoundError:
    os.system('pip install fastapi')
    os.system('pip install uvicorn')

finally:
    app = FastAPI()
    data = json.load(open('../db/db.json'))

    class API_PROJECT(BaseModel):
        @app.get('/', status_code=status.HTTP_200_OK)
        def home():
            return data