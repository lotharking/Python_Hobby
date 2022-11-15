import requests
import datetime
import json
import logging

from prefect import task, flow

logging.basicConfig(level=logging.INFO)

@task(retries=3,retry_delay_seconds=30)
def extract():
    logging.info("Se obtiene respuesta de la API")
    raw = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    logging.info("Codigo de respuesta: {}".format(raw.status_code))
    raw = json.loads(raw.text)

    with open('.\\ETLPython\Projects\dataraw.json', 'w', encoding='utf-8') as file:
        json.dump(raw, file, ensure_ascii=False, indent=4)
    return raw

@task()
def transform(raw):
    logging.info("Ejecutando transformacion")
    transformed = raw['title']    

    with open('.\\ETLPython\Projects\datatransformed.json', 'w', encoding='utf-8') as file:
        json.dump(transformed, file, ensure_ascii=False, indent=4)
    return transformed

@task()
def load(transformed):
    logging.info("*INFO: Procede tarea load")
    logging.info("*****ATENCION*****")
    logging.info("titulo de objeto 1")
    logging.info(str(transformed))

#schedule = IntervalSchedule(interval=datetime.timedelta(minutes=1))

@flow(name="P2.1 JSONPlaceholder 1")
def load_flow():
    raw = extract()
    transformed = transform(raw)
    load(transformed)


load_flow()