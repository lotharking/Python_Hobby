import requests
from datetime import timedelta
import json

from prefect import task, Flow
from prefect.schedules import IntervalSchedule

schedule = IntervalSchedule(interval=timedelta(minutes=1))

@task(log_stdout=True, max_retries=3, retry_delay=timedelta(minutes=1), cache_for=timedelta(minutes=30))
def extract():
    print("*INFO: Se obtiene respuesta de la API")
    raw = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print("*INFO: Codigo de respuesta: {}".format(raw.status_code))
    raw = json.loads(raw.text)

    with open('.\\ETLPython\Projects\dataraw.json', 'w', encoding='utf-8') as file:
        json.dump(raw, file, ensure_ascii=False, indent=4)
    return raw

@task(log_stdout=True)
def transform(raw):
    print("*INFO: Ejecutando transformacion")
    transformed = raw['title']    

    with open('.\\ETLPython\Projects\datatransformed.json', 'w', encoding='utf-8') as file:
        json.dump(transformed, file, ensure_ascii=False, indent=4)
    return transformed

@task(log_stdout=True)
def load(transformed):
    print("*INFO: Procede tarea load")
    print("*INFO: *****ATENCION*****")
    print("*INFO: titulo de objeto 1")
    print(str(transformed))

with Flow("P2.1 JSONPlaceholder 1") as flow:
    raw = extract()
    transformed = transform(raw)
    load(transformed)


flow.run()