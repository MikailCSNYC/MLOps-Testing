import pandas as pd

################################################################
# Sample functions for testing purposes
################################################################


# returns the first 2 rows of the dataset
def first_two_rows(df):
    return df[:2]


# returns the shuffled rows of the dataset
def shuffle(df):
    return df.sample(frac=1).reset_index(drop=True)


# returns the result of joining two dfs on a given columns
def join_columns(left, right, column):
    return left.join(right, on=column)



