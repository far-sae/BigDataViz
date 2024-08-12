# BigDataViz/preprocess.py
import dask.dataframe as dd

def preprocess_data(data: dd.DataFrame, operations: dict) -> dd.DataFrame:
    """
    Apply preprocessing steps to the data.
    """
    if "filter" in operations:
        data = data[data[operations["filter"]["column"]] == operations["filter"]["value"]]
    if "normalize" in operations:
        data = (data - data.min()) / (data.max() - data.min())
    return data
