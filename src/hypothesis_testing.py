"""
hypothesis_testing.py

Statistical hypothesis tests used in the IPL Statistical Analysis project.

Implemented:
1. One-Proportion Z-Test
2. Independent Two-Sample T-Test
3. Chi-Square Goodness-of-Fit Test
4. Cohen's d Effect Size

Author: Kopparapu Bhargava Narasimha
"""

import numpy as np

from scipy.stats import (
    norm,
    ttest_ind,
    chisquare
)


def one_proportion_z_test(
    sample_proportion,
    sample_size,
    population_proportion=0.5
):
    """
    Perform one-proportion Z-test.

    Returns
    -------
    tuple
        (z_statistic, p_value)
    """

    se = np.sqrt(
        (
            population_proportion
            *
            (1 - population_proportion)
        )
        / sample_size
    )

    z = (
        sample_proportion
        - population_proportion
    ) / se

    p = 1 - norm.cdf(z)

    return z, p


def independent_t_test(
    sample1,
    sample2,
    equal_variance=False
):
    """
    Perform independent two-sample t-test.

    Returns
    -------
    tuple
        (t_statistic, p_value)
    """

    return ttest_ind(
        sample1,
        sample2,
        equal_var=equal_variance
    )


def chi_square_goodness_of_fit(
    observed,
    expected
):
    """
    Perform Chi-Square Goodness-of-Fit Test.

    Returns
    -------
    tuple
        (chi_square_statistic, p_value)
    """

    return chisquare(
        observed,
        expected
    )


def cohens_d(
    sample1,
    sample2
):
    """
    Compute Cohen's d effect size.

    Returns
    -------
    float
    """

    sample1 = np.asarray(sample1)
    sample2 = np.asarray(sample2)

    pooled_sd = np.sqrt(
        (
            np.var(
                sample1,
                ddof=1
            )
            +
            np.var(
                sample2,
                ddof=1
            )
        ) / 2
    )

    return (
        np.mean(sample1)
        -
        np.mean(sample2)
    ) / pooled_sd
