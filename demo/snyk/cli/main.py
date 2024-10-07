import pandas as pd
import numpy as np

def parse_container(jsonfile)->pd.DataFrame:
    # In this method, we'll read the json file and parse it into a dataframe
    df = pd.read_json(jsonfile)
    return df

