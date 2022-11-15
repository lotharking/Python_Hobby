import requests

from prefect import task, Flow

@task
def extract():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response = response.json()
    return response

@task
def load(response):
    output = response[0]['title']
    print("*****ATENCION*****")
    print("titulo de objeto 1")
    print(str(output))

with Flow("P1.1 JSONPlaceholder 1") as flow:
    raw = extract()
    load(raw)


flow.run()