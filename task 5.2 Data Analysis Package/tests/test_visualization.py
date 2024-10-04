import pandas as pd
from data_analysis_package.visualization import generate_histogram  # Updated to use correct function name

def test_generate_histogram():
    df = pd.DataFrame({'Values': [10, 20, 20, 40]})
    try:
        fig = generate_histogram(df, 'Values')  
        assert fig is not None, "Expected a figure object to be returned"
       
    except Exception as e:
        assert False, f"generate_histogram raised an exception: {e}"
