from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from estudo_celery.tasks import ola_mundo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], # Aceita todas as origens
    allow_methods=['*'], # Aceita todos os métodos
    allow_headers=['*'], # Aceita todos os cabeçalhos 
    allow_credentials=True, # Aceita credencias na requisição
)


@app.get('/')
def read_root():
    ola_mundo.delay()
    return {'message': 'Requisição enviada.'}
