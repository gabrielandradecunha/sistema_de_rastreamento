from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users
import os
from dotenv import load_dotenv
from app.core.setupdb import setupdb

load_dotenv()
url_frontend = os.getenv('URL_FRONTEND')

app = FastAPI()

origins = [
    str(url_frontend), 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(users.router, tags=["getuser"])

@app.get("/")
def read_root():
    return {"message": "API para o sistema de rastreamento de veiculos"}

# @app.get("/setupdb")
# def setup_db():
#     setupdb()