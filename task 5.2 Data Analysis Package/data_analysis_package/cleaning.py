import pandas as pd

def handle_missing_data(df, strategy="mean"):
   
    if strategy == "mean":
        return df.fillna(df.mean())
    elif strategy == "median":
        return df.fillna(df.median())
    elif strategy == "mode":
        return df.fillna(df.mode().iloc[0])
    elif strategy == "drop":
        return df.dropna()
    else:
        raise ValueError("Unsupported strategy!")
