import requests

from prefect import task, Flow, flow

@task
def extract():
    pass

@task
def load(response):
    pass

@flow
def load_flow():
    raw = extract()
    load(raw)


load_flow()