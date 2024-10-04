import pandas as pd
from data_analysis_package.cleaning import fill_missing, drop_duplicates

def test_fill_missing():
    df = pd.DataFrame({'Data': [5, None, 7, 8]})
    filled_df = fill_missing(df, method='mean')
    assert filled_df.isnull().sum().sum() == 0, "There are still missing values after filling"

def test_drop_duplicates():
    df = pd.DataFrame({'Data': [10, 10, 20, 30]})
    deduped_df = drop_duplicates(df)
    assert deduped_df.shape[0] == 3, f"Expected 3 rows after dropping duplicates, got {deduped_df.shape[0]}"
