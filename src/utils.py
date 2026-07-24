"""
utils.py

General utility functions for the IPL Statistical Analysis project.

Author: Kopparapu Bhargava Narasimha
"""

import pandas as pd


def print_heading(title):
    """
    Print a formatted section heading.
    """

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_subheading(title):
    """
    Print a formatted subsection heading.
    """

    print("\n" + "-" * 40)
    print(title)
    print("-" * 40)


def display_dataframe(df, rows=5):
    """
    Display first few rows of a dataframe.
    """

    return df.head(rows)


def missing_values(df):
    """
    Return missing value count.
    """

    return df.isnull().sum()


def dataset_dimensions(df):
    """
    Return dataset dimensions.
    """

    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1]
    }


def dataset_info(df):
    """
    Return dataset summary.
    """

    return pd.DataFrame({
        "Data Type": df.dtypes,
        "Missing Values": df.isnull().sum(),
        "Unique Values": df.nunique()
    })
