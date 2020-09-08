import pandas as pd

def drop_record(olympics):
    new_series = olympics.drop(index=2020)
    return new_series
