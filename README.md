Sales Data Analysis using Pandas

📊 Project Description

This project analyzes sales data using Python and Pandas.
The goal is to understand total sales, top products, and sales performance in different cities.

🛠 Technologies Used

* Python
* Pandas
* NumPy

📁 Dataset

The dataset contains the following columns:

* Date
* City
* Product
* Units_Sold
* Price

⚙️ Steps in the Project

1. Load the dataset using Pandas
2. Clean and prepare the data
3. Create a new column **Total_Sales**
4. Calculate total sales by city
5. Find top selling products

💻 Example Code

df["Total_Sales"] = df["Units_Sold"] * df["Price"]

city_sales = df.groupby("City")["Total_Sales"].sum()

top_product = df.groupby("Product")["Units_Sold"].sum().sort_values(ascending=False)

📈 Output

* Total sales by city
* Top selling products
* Daily sales summary

🎯 Conclusion

This project demonstrates how Pandas can be used for basic sales data analysis and business insights.

👨‍💻 Author

Manoj
