"""
confidence_intervals.py

Confidence interval calculations used in the IPL Statistical Analysis project.

Implemented:
1. Z-Confidence Interval for Population Proportion
2. T-Confidence Interval for Population Mean

Author: Kopparapu Bhargava Narasimha
"""

import numpy as np
from scipy.stats import norm, t


def proportion_confidence_interval(
    p_hat,
    sample_size,
    confidence_level=0.95
):
    """
    Compute confidence interval for a population proportion.

    Parameters
    ----------
    p_hat : float
        Sample proportion.

    sample_size : int
        Sample size.

    confidence_level : float
        Confidence level (default = 95%).

    Returns
    -------
    tuple
        (lower_bound, upper_bound)
    """

    alpha = 1 - confidence_level

    z = norm.ppf(1 - alpha / 2)

    se = np.sqrt((p_hat * (1 - p_hat)) / sample_size)

    margin = z * se

    return (
        p_hat - margin,
        p_hat + margin
    )


def mean_confidence_interval(
    data,
    confidence_level=0.95
):
    """
    Compute confidence interval for a population mean using t-distribution.

    Parameters
    ----------
    data : array-like

    confidence_level : float

    Returns
    -------
    tuple
        (lower_bound, upper_bound)
    """

    data = np.asarray(data)

    n = len(data)

    mean = np.mean(data)

    se = np.std(
        data,
        ddof=1
    ) / np.sqrt(n)

    alpha = 1 - confidence_level

    t_value = t.ppf(
        1 - alpha / 2,
        n - 1
    )

    margin = t_value * se

    return (
        mean - margin,
        mean + margin
    )
