from prefect import task, Flow, flow

@task
def load():
    pass
"""
with Flow("P1.1 - Hello World") as flow:
    load()
    
flow.run()
"""

@flow
def flow_caso():
    load()
 
flow_caso()