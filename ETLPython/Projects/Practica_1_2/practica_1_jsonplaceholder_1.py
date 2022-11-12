import requests

from prefect import task, Flow, flow

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

@flow
def load_flow():
    raw = extract()
    load(raw)


load_flow()