"""
sampling.py

Sampling techniques for statistical analysis.

Implements:
1. Simple Random Sampling
2. Systematic Sampling
3. Stratified Sampling

Author: Kopparapu Bhargava Narasimha
Project: IPL Statistical Analysis using Python
"""

import pandas as pd


def simple_random_sampling(df, sample_size, random_state=42):
    """
    Perform Simple Random Sampling.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    sample_size : int
        Number of rows to sample.

    random_state : int
        Seed for reproducibility.

    Returns
    -------
    pandas.DataFrame
        Random sample.
    """

    if sample_size > len(df):
        raise ValueError("Sample size cannot exceed dataset size.")

    return df.sample(
        n=sample_size,
        random_state=random_state
    ).reset_index(drop=True)


def systematic_sampling(df, sample_size):
    """
    Perform Systematic Sampling.

    Parameters
    ----------
    df : pandas.DataFrame

    sample_size : int

    Returns
    -------
    pandas.DataFrame
    """

    population = len(df)

    if sample_size > population:
        raise ValueError("Sample size cannot exceed dataset size.")

    step = population // sample_size

    sample = df.iloc[::step].head(sample_size)

    return sample.reset_index(drop=True)


def stratified_sampling(
        df,
        stratify_column,
        sample_fraction=0.2,
        random_state=42
):
    """
    Perform Stratified Sampling.

    Parameters
    ----------
    df : pandas.DataFrame

    stratify_column : str
        Column used for stratification.

    sample_fraction : float
        Fraction of each group to sample.

    random_state : int

    Returns
    -------
    pandas.DataFrame
    """

    if stratify_column not in df.columns:
        raise ValueError(
            f"'{stratify_column}' not found in dataset."
        )

    sample = (
        df.groupby(stratify_column, group_keys=False)
          .apply(
              lambda x: x.sample(
                  frac=sample_fraction,
                  random_state=random_state
              )
          )
    )

    return sample.reset_index(drop=True)


def compare_sample_sizes(population_size, sample_df):
    """
    Compare population and sample sizes.

    Parameters
    ----------
    population_size : int

    sample_df : pandas.DataFrame

    Returns
    -------
    dict
    """

    return {
        "Population Size": population_size,
        "Sample Size": len(sample_df),
        "Sampling Percentage":
            round((len(sample_df) / population_size) * 100, 2)
    }


def sampling_summary(sample_df):
    """
    Display summary of sampled dataset.

    Parameters
    ----------
    sample_df : pandas.DataFrame
    """

    print("=" * 60)
    print("Sample Summary")
    print("=" * 60)

    print(f"Rows    : {sample_df.shape[0]}")
    print(f"Columns : {sample_df.shape[1]}")

    print("\nMissing Values")
    print(sample_df.isnull().sum())

    print("\nData Types")
    print(sample_df.dtypes)
