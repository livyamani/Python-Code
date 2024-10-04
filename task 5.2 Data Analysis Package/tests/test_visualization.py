import pandas as pd
from data_analysis_package.visualization import plot_histogram

def test_plot_histogram():
    df = pd.DataFrame({'Values': [10, 20, 20, 40]})
    try:
        plot_histogram(df, 'Values')  # Check if plot is generated without errors
    except Exception as e:
        assert False, f"plot_histogram raised an exception: {e}"
