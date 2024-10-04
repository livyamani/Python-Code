import pandas as pd
from data_analysis_package.cleaning import handle_missing_data, drop_duplicates  # Update this line

def test_handle_missing_data():
    df = pd.DataFrame({'Data': [5, None, 7, 8]})
    filled_df = handle_missing_data(df, strategy='mean')  # Ensure the method matches the function
    assert filled_df.isnull().sum().sum() == 0, "There are still missing values after filling"

def test_drop_duplicates():
    df = pd.DataFrame({'Data': [10, 10, 20, 30]})
    deduped_df = drop_duplicates(df)
    assert deduped_df.shape[0] == 3, f"Expected 3 rows after dropping duplicates, got {deduped_df.shape[0]}"
