import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

os.makedirs("visualizations", exist_ok=True)

df = pd.read_csv("/content/sales_data.csv")

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print(df.head())

print("\nColumns:")
print(df.columns)

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.strftime("%b")

sns.set_style("whitegrid")


plt.figure(figsize=(10,6))

sales_product = df.groupby("Product")["Total_Sales"].sum().sort_values()

sns.barplot(
    x=sales_product.index,
    y=sales_product.values,
    palette="viridis"
)

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("visualizations/sales_by_product.png")

plt.show()


monthly_sales = df.groupby("Month")["Total_Sales"].sum()

plt.figure(figsize=(10,6))

sns.lineplot(
    x=monthly_sales.index,
    y=monthly_sales.values,
    marker="o",
    linewidth=3,
    color="blue"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("visualizations/monthly_sales.png")

plt.show()


plt.figure(figsize=(10,6))

sns.boxplot(
    x="Region",
    y="Total_Sales",
    data=df,
    palette="Set2"
)

plt.title("Sales Distribution by Region")

plt.tight_layout()

plt.savefig("visualizations/boxplot.png")

plt.show()


plt.figure(figsize=(10,6))

sns.violinplot(
    x="Product",
    y="Total_Sales",
    data=df,
    palette="coolwarm"
)

plt.title("Product Sales Distribution")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("visualizations/violinplot.png")

plt.show()


plt.figure(figsize=(8,6))

corr = df[["Quantity","Price","Total_Sales"]].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="YlGnBu",
    linewidths=1
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("visualizations/heatmap.png")

plt.show()


plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df,
    x="Price",
    y="Total_Sales",
    hue="Region",
    size="Quantity"
)

plt.title("Price vs Total Sales")

plt.tight_layout()

plt.savefig("visualizations/scatter_plot.png")

plt.show()


fig, axes = plt.subplots(2,2, figsize=(15,10))

sns.barplot(
    data=df,
    x="Product",
    y="Total_Sales",
    ax=axes[0,0]
)
axes[0,0].set_title("Sales by Product")
axes[0,0].tick_params(axis='x', rotation=30)

sns.boxplot(
    data=df,
    x="Region",
    y="Total_Sales",
    ax=axes[0,1]
)
axes[0,1].set_title("Region Distribution")

sns.violinplot(
    data=df,
    x="Product",
    y="Total_Sales",
    ax=axes[1,0]
)
axes[1,0].set_title("Product Distribution")
axes[1,0].tick_params(axis='x', rotation=30)

sns.scatterplot(
    data=df,
    x="Price",
    y="Total_Sales",
    hue="Region",
    ax=axes[1,1]
)
axes[1,1].set_title("Price vs Sales")

plt.tight_layout()

plt.savefig("visualizations/dashboard.png")

plt.show()


fig = px.scatter(
    df,
    x="Price",
    y="Total_Sales",
    color="Region",
    size="Quantity",
    hover_name="Product",
    hover_data=["Customer_ID"],
    title="Interactive Sales Dashboard"
)

fig.show()

fig = px.bar(
    df,
    x="Product",
    y="Total_Sales",
    color="Region",
    title="Interactive Product Sales"
)

fig.show()


fig = px.pie(
    df,
    names="Product",
    values="Total_Sales",
    title="Sales Contribution by Product"
)

fig.show()


print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

print("\nHighest Selling Product:")
print(df.groupby("Product")["Total_Sales"].sum().idxmax())

print("\nHighest Sales Region:")
print(df.groupby("Region")["Total_Sales"].sum().idxmax())

print("\nTotal Revenue:")
print(df["Total_Sales"].sum())

print("\nAverage Sale:")
print(round(df["Total_Sales"].mean(),2))

print("\nHighest Sale:")
print(df["Total_Sales"].max())

print("\nLowest Sale:")
print(df["Total_Sales"].min())

print("\nTop 5 Customers:")
print(df.groupby("Customer_ID")["Total_Sales"].sum().sort_values(ascending=False).head())

print("\nDashboard Completed Successfully!")
