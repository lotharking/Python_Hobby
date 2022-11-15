import requests
import datetime

from prefect import task, flow

@task(retries=3,retry_delay_seconds=30)
def extract():
    print("*INFO: Se obtiene respuesta de la API")
    raw = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("*INFO: Codigo de respuesta: {}".format(response.status_code))
    raw = raw.json()
    return raw

@task()
def transform(raw):
    print("*INFO: Ejecutando transformacion")
    transformed = raw[0]['title']
    return transformed


@task()
def load(transformed):
    print("*INFO: Procede tarea load")
    print("*****ATENCION*****")
    print("titulo de objeto 1")
    print(str(transformed))

@flow(name="P2.1 JSONPlaceholder 1")
def load_flow():
    raw = extract()
    transform = transform(raw)
    load(transform)


load_flow()