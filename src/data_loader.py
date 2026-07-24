"""
data_loader.py

Utility functions for loading and inspecting IPL datasets.

Author: Kopparapu Bhargava Narasimha
Project: IPL Statistical Analysis using Python
"""

from pathlib import Path
import pandas as pd


# -----------------------------------------------------------------------------
# Dataset Paths
# -----------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"


# -----------------------------------------------------------------------------
# Dataset Loading Functions
# -----------------------------------------------------------------------------

def load_ipl():
    """
    Load IPL.csv dataset.

    Returns
    -------
    pandas.DataFrame
    """
    path = DATA_DIR / "IPL.csv"

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    return pd.read_csv(path)


def load_matches():
    """
    Load matches.csv dataset.

    Returns
    -------
    pandas.DataFrame
    """
    path = DATA_DIR / "matches.csv"

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    return pd.read_csv(path)


def load_deliveries():
    """
    Load deliveries.csv dataset.

    Returns
    -------
    pandas.DataFrame
    """
    path = DATA_DIR / "deliveries.csv"

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    return pd.read_csv(path)


# -----------------------------------------------------------------------------
# Load All Datasets
# -----------------------------------------------------------------------------

def load_all():
    """
    Load all IPL datasets.

    Returns
    -------
    tuple
        (ipl_df, matches_df, deliveries_df)
    """
    return (
        load_ipl(),
        load_matches(),
        load_deliveries(),
    )


# -----------------------------------------------------------------------------
# Dataset Summary
# -----------------------------------------------------------------------------

def dataset_summary(df, name="Dataset"):
    """
    Print a concise summary of a dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset.

    name : str
        Dataset name.
    """

    print("=" * 60)
    print(name)
    print("=" * 60)

    print(f"Rows       : {df.shape[0]}")
    print(f"Columns    : {df.shape[1]}")

    memory_mb = df.memory_usage(deep=True).sum() / 1024**2
    print(f"Memory     : {memory_mb:.2f} MB")

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nData Types")
    print(df.dtypes)


# -----------------------------------------------------------------------------
# Preview Dataset
# -----------------------------------------------------------------------------

def preview(df, rows=5):
    """
    Display first few rows.

    Parameters
    ----------
    df : pandas.DataFrame

    rows : int
        Number of rows to display.
    """
    return df.head(rows)


# -----------------------------------------------------------------------------
# Dataset Shape
# -----------------------------------------------------------------------------

def dataset_shape(df):
    """
    Return dataset dimensions.

    Returns
    -------
    tuple
    """
    return df.shape
