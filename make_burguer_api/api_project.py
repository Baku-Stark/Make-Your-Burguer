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
        # MainURL: http://127.0.0.1:8000
        @app.get('/ingredientes', status_code=status.HTTP_200_OK)
        def home():
            return data