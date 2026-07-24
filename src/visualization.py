"""
visualization.py

Visualization utilities for the IPL Statistical Analysis project.

Author: Kopparapu Bhargava Narasimha
"""

import matplotlib.pyplot as plt
import numpy as np


def boxplot_comparison(
    sample1,
    sample2,
    labels=("Sample 1", "Sample 2"),
    title="Boxplot Comparison",
    ylabel="Value"
):
    """
    Plot a boxplot comparing two samples.
    """

    plt.figure(figsize=(7, 5))

    plt.boxplot(
        [sample1, sample2],
        tick_labels=list(labels)
    )

    plt.title(title)
    plt.ylabel(ylabel)

    plt.tight_layout()
    plt.show()


def observed_vs_expected(
    observed,
    expected,
    xlabel="Category",
    ylabel="Frequency",
    title="Observed vs Expected Frequencies"
):
    """
    Plot observed and expected frequencies side by side.
    """

    x = np.arange(len(observed))

    plt.figure(figsize=(8, 5))

    plt.bar(
        x - 0.2,
        observed,
        width=0.4,
        label="Observed"
    )

    plt.bar(
        x + 0.2,
        expected,
        width=0.4,
        label="Expected"
    )

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.legend()

    plt.tight_layout()
    plt.show()


def histogram(
    data,
    bins=20,
    title="Histogram",
    xlabel="Value",
    ylabel="Frequency"
):
    """
    Plot histogram.
    """

    plt.figure(figsize=(7, 5))

    plt.hist(
        data,
        bins=bins
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.tight_layout()
    plt.show()


def save_current_figure(path, dpi=300):
    """
    Save current matplotlib figure.
    """

    plt.savefig(
        path,
        dpi=dpi,
        bbox_inches="tight"
    )
