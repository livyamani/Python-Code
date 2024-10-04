import pandas as pd
from data_analysis_package.statistics import correlation, t_test

def test_correlation():
    df = pd.DataFrame({'X': [1, 3, 5], 'Y': [2, 4, 6]})
    result = correlation(df, 'X', 'Y')
    assert round(result, 2) == 1.0, f"Expected correlation of 1.0, got {result}"

def test_t_test():
    group1 = [2, 4, 6]
    group2 = [1, 2, 3]
    _, p_value = t_test(group1, group2)
    assert p_value > 0.05, "Expected p-value > 0.05 indicating no significant difference"
