from celery import Celery

app_celery = Celery(
    broker='pyamqp://guest@localhost//',
    backend='db+mysql+pymysql://root:1234@127.0.0.1:3306/database_sto',
    result_extended=True  # Habilita metadados estendidos
)

@app_celery.task(name='ola mundo')
def ola_mundo():
    return 'olá mundo'
