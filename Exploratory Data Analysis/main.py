import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

"""
Load dataset for exploratory analysis.
"""
df = pd.read_csv("marmara2.csv")

os.makedirs("Images", exist_ok=True)
plot_id = 1


"""
DATA STRUCTURE OVERVIEW
Displays dataset structure and descriptive statistics.
"""
print("\n=== DATA INFO ===\n")
print(df.info())

print("\n=== DESCRIBE ===\n")
print(df.describe())


"""
CENTRAL TENDENCY ANALYSIS
Mean and median for numerical variables.
"""
print("\n=== MEAN ===\n")
print(df.mean(numeric_only=True))

print("\n=== MEDIAN ===\n")
print(df.median(numeric_only=True))


"""
VARIABILITY ANALYSIS
Standard deviation and variance for dispersion measurement.
"""
print("\n=== STANDARD DEVIATION ===\n")
print(df.std(numeric_only=True))

print("\n=== VARIANCE ===\n")
print(df.var(numeric_only=True))


"""
MISSING VALUES CHECK
Ensures dataset completeness.
"""
print("\n=== MISSING VALUES ===\n")
print(df.isnull().sum())


"""
DISTRIBUTION ANALYSIS
Histograms for all numerical features.
"""
df.drop(columns=["species"]).hist(bins=15, figsize=(10,6))
plt.suptitle("Feature Distributions")
plt.tight_layout()
plt.savefig(f"Images/plot_{plot_id}_hist.png", dpi=300, bbox_inches="tight")
plot_id += 1
plt.show()


"""
OUTLIER ANALYSIS
Boxplots with hidden extreme markers for better readability.
"""
df.drop(columns=["species"]).boxplot(figsize=(10,5), showfliers=False)
plt.xticks(rotation=45)
plt.title("Outlier Structure (IQR-based view)")
plt.tight_layout()
plt.savefig(f"Images/plot_{plot_id}_boxplot.png", dpi=300, bbox_inches="tight")
plot_id += 1
plt.show()


"""
CORRELATION ANALYSIS
Heatmap with balanced color scaling for interpretability.
"""
corr = df.corr(numeric_only=True)

print("\n=== CORRELATION MATRIX ===\n")
print(corr)

cov = df.cov(numeric_only=True)

print("\n=== COVARIANCE MATRIX ===\n")
print(cov)

plt.figure(figsize=(8,5))
sns.heatmap(corr, cmap="RdBu_r", center=0, linewidths=0.3)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(f"Images/plot_{plot_id}_heatmap.png", dpi=300, bbox_inches="tight")
plot_id += 1
plt.show()


"""
RELATIONSHIP ANALYSIS
Length vs weight with reduced overlap for clarity.
"""
plt.figure(figsize=(6,4))
plt.scatter(
    df["total_length_cm"],
    df["weight_gr"],
    s=10,
    alpha=0.35,
    edgecolors="none"
)
plt.xlabel("Total Length (cm)")
plt.ylabel("Weight (g)")
plt.title("Length vs Weight Relationship")
plt.tight_layout()
plt.savefig(f"Images/plot_{plot_id}_scatter.png", dpi=300, bbox_inches="tight")
plot_id += 1
plt.show()


"""
CATEGORY DISTRIBUTION
Species frequency distribution.
"""
print("\n=== SPECIES COUNT ===\n")
print(df["species"].value_counts())

df["species"].value_counts().plot(kind="bar")
plt.title("Species Distribution")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(f"Images/plot_{plot_id}_bar.png", dpi=300, bbox_inches="tight")
plot_id += 1
plt.show()


"""
GROUP ANALYSIS
Mean values per species.
"""
print("\n=== MEAN VALUES PER SPECIES ===\n")
print(df.groupby("species").mean(numeric_only=True))