from prefect import task, Flow, flow

@task
def load():
    print("Hello World")

with Flow("P1.1 - Hello World") as flow:
    load()
    
flow.run()
