import pandas as pd
data = pd.read_csv("sales.csv")
data["Total_sales"] = data["Units_Sold"] * data["Price"]
City_sales = data.groupby("City")["Total_sales"].sum()
top_products = data.groupby("Product")["Units_Sold"].sum().sort_values(ascending=False)
daily_sales = data.groupby("Date")["Total_sales"].sum()
print(daily_sales)
print(top_products)
