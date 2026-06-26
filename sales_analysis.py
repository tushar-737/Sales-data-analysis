
import pandas as pd

# -------------------------------
# Step 1 : Load Dataset
# -------------------------------
df = pd.read_csv("sales_data.csv")

print("=" * 50)
print("Sales Data Analysis")
print("=" * 50)

# -------------------------------
# Step 2 : Explore Dataset
# -------------------------------
print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nShape of Dataset")
print(df.shape)

print("\nColumn Names")
print(df.columns)

# -------------------------------
# Step 3 : Check Missing Values
# -------------------------------
print("\nMissing Values")
print(df.isnull().sum())

# Fill missing values (if any)
df.fillna(0, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# -------------------------------
# Step 4 : Basic Statistics
# -------------------------------
print("\nStatistics")
print(df.describe())

# -------------------------------
# Step 5 : Analysis
# -------------------------------

# Total Revenue
total_revenue = df["Total_Sales"].sum()

# Average Revenue
average_sales = df["Total_Sales"].mean()

# Highest Sale
highest_sale = df["Total_Sales"].max()

# Lowest Sale
lowest_sale = df["Total_Sales"].min()

# Best Selling Product
best_product = df.groupby("Product")["Quantity"].sum().idxmax()

# Quantity Sold
best_quantity = df.groupby("Product")["Quantity"].sum().max()

# Revenue by Region
region_sales = df.groupby("Region")["Total_Sales"].sum()

# -------------------------------
# Step 6 : Final Report
# -------------------------------
print("\n")
print("=" * 50)
print("SALES REPORT")
print("=" * 50)

print(f"Total Revenue      : ₹{total_revenue:,.2f}")
print(f"Average Sale       : ₹{average_sales:,.2f}")
print(f"Highest Sale       : ₹{highest_sale:,.2f}")
print(f"Lowest Sale        : ₹{lowest_sale:,.2f}")
print(f"Best Product       : {best_product}")
print(f"Units Sold         : {best_quantity}")

print("\nRevenue by Region")
print(region_sales)

print("=" * 50)