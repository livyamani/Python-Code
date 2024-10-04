import matplotlib.pyplot as plt
import seaborn as sns

def generate_histogram(data, column, bins=10):
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], bins=bins)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    
    fig = plt.gcf()
    plt.close()  # Close the plot to free up memory
    return fig

def generate_scatter_plot(data, x_column, y_column):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data[x_column], y=data[y_column])
    plt.title(f'Scatter plot of {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    
    fig = plt.gcf()
    plt.close()  # Close the plot to free up memory
    return fig 