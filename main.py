import matplotlib.pyplot as plt
import pandas as pd

download_url = (
    "https://raw.githubusercontent.com/fivethirtyeight/"
    "data/master/college-majors/recent-grads.csv"
)

df = pd.read_csv(download_url)

type(df)

# make sure pandas doesn’t hide any columns
pd.set_option("display.max.columns", None)

df.head()

# Line graph
df.plot(x="Rank", y=["P25th", "Median", "P75th"])
plt.show()

# Histogram
median_column = df["Median"]
type(median_column)
median_column.plot(kind="hist")
plt.show()

# Outliers
top_5 = df.sort_values(by="Median", ascending=False).head()
top_5.plot(x="Major", y="Median", kind="bar", rot=5, fontsize=4)
plt.show()

# investigate all majors whose median salary is above $60,000
top_medians = df[df["Median"] > 60000].sort_values("Median")
top_medians.plot(x="Major", y=["P25th", "Median", "P75th"], kind="bar")
plt.show()

# Check for Correlation
df.plot(x="Median", y="Unemployment_rate", kind="scatter")

# Analyze Categorical Data
cat_totals = df.groupby("Major_category")["Total"].sum().sort_values()

print(cat_totals)

cat_totals.plot(kind="barh", fontsize=4)

# Determining Ratios
small_cat_totals = cat_totals[cat_totals < 100_000]
big_cat_totals = cat_totals[cat_totals > 100_000]

# Adding a new item "Other" with the sum of the small categories
small_sums = pd.Series([small_cat_totals.sum()], index=["Other"])
big_cat_totals = big_cat_totals.append(small_sums)
big_cat_totals.plot(kind="pie", label="")
plt.show()

# Zooming in on Categories
df[df["Major_category"] == "Engineering"]["Median"].plot(kind="hist")