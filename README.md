# IPL Statistical Analysis using Python

A comprehensive statistical analysis project on the Indian Premier League (IPL) dataset, demonstrating the application of sampling techniques, statistical inference, hypothesis testing, confidence intervals, and probability distributions using Python.

This project was developed to apply core statistical concepts on real-world cricket data and derive meaningful insights through exploratory analysis and inferential statistics.

---

## Project Objectives

- Perform statistical analysis on IPL match data.
- Apply different sampling techniques and compare their effectiveness.
- Estimate population parameters using confidence intervals.
- Conduct hypothesis testing to validate statistical claims.
- Analyze cricket events using probability distributions.
- Visualize data to communicate statistical insights effectively.

---

## Research Questions

1. Does winning the toss significantly increase the probability of winning an IPL match?
2. Is batting first associated with a higher chance of winning?
3. Can the number of wickets per over in IPL matches be modeled using a Poisson distribution?

## Dataset

This project uses the publicly available IPL datasets from Kaggle.

Datasets used:

- `ipl_data.csv`
- `matches.csv`
- `deliveries.csv`

The datasets contain information about:

- IPL matches
- Ball-by-ball deliveries
- Match outcomes
- Players
- Teams
- Runs
- Wickets
- Toss information
- Venues
- Innings statistics

The datasets are included in the `data/` directory for reproducibility.

Original source:
https://www.kaggle.com/datasets

*(The datasets are publicly available on Kaggle. Please refer to Kaggle for the original source and licensing information.)*

---

## Project Workflow

```
Dataset Collection
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Population Analysis
        │
        ▼
Sampling Techniques
        │
        ▼
Confidence Interval Estimation
        │
        ▼
Hypothesis Testing
        │
        ▼
Probability Distribution Analysis
        │
        ▼
Visualization & Statistical Insights
```

---

## Statistical Concepts Implemented

### Sampling Techniques

- Simple Random Sampling
- Systematic Sampling
- Stratified Sampling

### Statistical Measures

- Mean
- Median
- Mode
- Variance
- Standard Deviation

### Confidence Intervals

- Population Mean Estimation
- Margin of Error
- Confidence Interval Construction

### Hypothesis Testing

- Z-Test
- T-Test
- Chi-Square Test

### Probability Distribution

- Poisson Distribution

---

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- SciPy
- Matplotlib

---

## Repository Structure

```
ipl-statistical-analysis/

│
├── data/
│   ├── ipl_data.csv
│   ├── deliveries.csv #you have to download
│   └── matches.csv
│
├── notebooks/
│   └── IPL_Statistical_Analysis.ipynb
│
├── src/
│   ├── confidence_intervals.py/
│   ├── data_loader.py/
|   ├── hypothesis_testing.py/
|   ├── sampling.py/
|   └── utils.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Key Features

- End-to-end statistical analysis on real IPL datasets.
- Comparison of multiple sampling techniques.
- Confidence interval estimation for population parameters.
- Statistical hypothesis testing using Python.
- Data visualization for better interpretation of results.
- Well-documented Jupyter Notebook with reproducible analysis.

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/ipl-statistical-analysis.git
```

Navigate to the project directory

```bash
cd IPL-Statistical-Analysis
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

---

## Results

The project demonstrates the practical application of statistical inference techniques on real-world cricket data.

The analysis includes:

- Population analysis
- Comparison of sampling methods
- Confidence interval estimation
- Hypothesis testing
- Probability distribution modelling
- Statistical visualization

---

## Future Improvements

- Develop an interactive Streamlit dashboard.
- Add bootstrap sampling methods.
- Implement additional statistical tests.
- Include advanced visual analytics.
- Automate report generation.

---

## Author

**Kopparapu Bhargava Narasimha**

B.E Artificial Intelligence & Machine Learning

BMS College of Engineering

---

## License

This project is licensed under the MIT License.
