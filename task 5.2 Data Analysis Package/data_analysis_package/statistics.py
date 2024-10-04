import scipy.stats as stats

def perform_ttest(sample1, sample2):
    t_stat, p_value = stats.ttest_ind(sample1, sample2)
    return t_stat, p_value

def calculate_correlation(data, column1, column2):
    return data[column1].corr(data[column2])
