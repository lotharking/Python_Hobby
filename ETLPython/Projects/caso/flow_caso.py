# Import libraries and enviroment variables

import pandas as pd
import numpy as nd

from prefect import task, Flow

# Extract of data
@task
def extract():
    pass

# Transform
def transform():
    pass

# Load
def load():
    pass

# Flow
with Flow("ETL caso") as flow:
    raw_dfs = extract()
    tablon = transform(raw_dfs)
    load(tablon)

flow.run()