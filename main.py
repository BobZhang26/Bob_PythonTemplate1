"""
Main cli or app entry point
"""

import pandas as pd

# define a function to provide descriptive statistics of a dataset


def pd_descriptive(file):
    data = pd.read_csv(file)
    return data.describe()


# if __name__ == "__main__":
# pylint: disable=no-value-for-parameter
#     add_cli()
