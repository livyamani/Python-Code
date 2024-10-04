import pandas as pd
from data_analysis_package.cleaning import handle_missing_data
from data_analysis_package.visualization import generate_histogram
from data_analysis_package.statistics import perform_ttest  # Updated to match the function name

# Define a sample dataset
sample_data = pd.DataFrame({
    'height': [5.5, 6.0, None, 5.8, 6.2],
    'weight': [150, 160, 155, None, 165]
})

# Clean the data by addressing missing values
cleaned_sample = handle_missing_data(sample_data, strategy='median')
print("Cleaned Dataset:")
print(cleaned_sample)

# Generate a histogram to visualize height data
generate_histogram(cleaned_sample, 'height')

# Conduct a t-test on the height and weight data
statistic, p_val = perform_ttest(cleaned_sample['height'].dropna(), cleaned_sample['weight'].dropna())
print(f"Statistical Result: T-statistic = {statistic}, P-value = {p_val}")
