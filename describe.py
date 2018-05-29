#!/usr/bin/env python3

"""
Module to display some general characteristics on numeric columns.
Author: Marijke
"""

import import_xlsx as i_x
from sys import argv


def describe(df, col="None"):
    """ Returns count, mean, std, min, 25%, 50%, 75% and max.

    df -- df, dataframe
    col -- string, numerical column, default: None (select whole df)
    """
    if col == "None":
        result = xlsx_df.describe()
    else:
        result = xlsx_df[col].describe()
    return(result)


if __name__ == "__main__":
    xlsx_df = i_x.import_xlsx(argv[1])
    column = "N_campione"

    print(describe(xlsx_df))
    print(describe(xlsx_df, column))
    print(describe(xlsx_df, column)[1]) # to select mean
    print(describe(xlsx_df, column)[1:3]) # to select mean and std
