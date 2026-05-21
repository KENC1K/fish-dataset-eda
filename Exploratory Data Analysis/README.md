
# Fish Dataset Exploratory Data Analysis

## Overview
This project performs an **Exploratory Data Analysis (EDA)** on a fish dataset stored in `marmara2.csv`.
The analysis focuses on:

- Understanding the dataset structure
- Descriptive statistics
- Central tendency measurements
- Variability analysis
- Missing value inspection
- Distribution analysis
- Outlier detection
- Correlation and covariance analysis
- Relationship visualization between variables
- Species distribution analysis
- Grouped statistical analysis by species

The script automatically generates and saves visualizations into an `Images/` directory.

---

## Technologies Used

- Python 3
- Pandas
- Matplotlib
- Seaborn

---

## Project Structure

```text
project/
│
├── marmara2.csv
├── main.py
├── requirements.txt
├── README.md
└── Images/
    ├── plot_1_hist.png
    ├── plot_2_boxplot.png
    ├── plot_3_heatmap.png
    ├── plot_4_scatter.png
    └── plot_5_bar.png
````

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a virtual environment (optional but recommended)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Dataset Requirements

The dataset file must be named:

```text
marmara2.csv
```

The dataset should contain at least the following columns:

* `species`
* `total_length_cm`
* `weight_gr`

Additional numerical columns are also supported.

---

## Running the Project

Run the script using:

```bash
python main.py
```

---

## Analysis Performed

### 1. Dataset Structure Overview

Displays:

* Dataset information
* Data types
* Statistical summary

Functions used:

* `df.info()`
* `df.describe()`

---

### 2. Central Tendency Analysis

Calculates:

* Mean
* Median

For all numerical variables.

---

### 3. Variability Analysis

Calculates:

* Standard deviation
* Variance

To measure data dispersion.

---

### 4. Missing Values Check

Detects missing values in the dataset using:

```python
df.isnull().sum()
```

---

### 5. Distribution Analysis

Generates histograms for numerical variables.

Output:

```text
Images/plot_1_hist.png
```

---

### 6. Outlier Analysis

Generates boxplots for detecting outliers.

Output:

```text
Images/plot_2_boxplot.png
```

---

### 7. Correlation Analysis

Computes:

* Correlation matrix
* Covariance matrix

And visualizes correlations using a heatmap.

Output:

```text
Images/plot_3_heatmap.png
```

---

### 8. Relationship Analysis

Visualizes the relationship between:

* Total length
* Weight

Using a scatter plot.

Output:

```text
Images/plot_4_scatter.png
```

---

### 9. Species Distribution

Displays species frequencies using a bar chart.

Output:

```text
Images/plot_5_bar.png
```

---

### 10. Group Analysis

Calculates mean numerical values grouped by species.

Example:

```python
df.groupby("species").mean(numeric_only=True)
```

---

## Generated Outputs

The script automatically saves all plots in the `Images/` folder with high resolution (`300 DPI`).

---

## Example Output

Console outputs include:

* Statistical summaries
* Correlation matrix
* Covariance matrix
* Missing value counts
* Species counts
* Grouped averages

---

## Future Improvements

Possible future enhancements:

* Interactive visualizations
* Machine learning classification
* Data preprocessing pipeline
* Advanced statistical testing
* Exporting reports to PDF

## License

This project is open-source and available under the MIT License.

````
