import pandas as pd
import json 

def read_csv(file_path):
    return pd.read_csv(file_path).to_dict(orient="records")

def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
