# Analysis Sales Data - 1 & 2 using python(pandas, numpy)
# Analysis Sales Data - 1

This program analyzes sales data to identify trends and patterns.

### Data Details

The data is assumed to be a CSV file named "sales_data.csv" containing the following columns:

- Product: Name of the product
- Quantity: Number of units sold
- Price: Price per unit
- Date: Date of the sale (format: YYYY-MM-DD)

### Steps to follow :

- Import pandas and numpy

``` 
import pandas as pd
import numpy as np
```

- load_product_data(filename):
 This function takes a filename as input and uses pandas to read the CSV data into a DataFrame.



```
from google.colab import drive
drive.mount("/content/drive")

def load_data(sales_data_path):
  sales_data_path = ("/content/drive/MyDrive/Python_Project/sales_data.csv")
  sales = pd.read_csv(sales_data_path)
  return sales
#load_data(sales)

```

- calculate_total_sales(data): 
This function takes a DataFrame containing sales data and calculates the total sales amount for each product. It should return a new DataFrame with a "Total Sales" column.

``` 
def calculate_total_sales(data):
  sales_data_path['total_sales'] = sales_data_path["Quantity"] * sales_data_path["Price"]
  return sales_data_path
  #sales_data_path
  ```

- find_top_selling_products(data, num_products=5): 
This function takes a DataFrame containing sales data and an optional parameter for the number of products (default 5) as input. It identifies the top-selling products based on total sales amount. The function should return a list of product names sorted by descending sales.prices.

```
#find_top_selling_products(data, num_products=5)

import numpy as np
def find_top_selling_products(data, num_products=5):
  sales_data_path['total_sales'] = sales_data_path["Quantity"] * sales_data_path["Price"]
  sales_sorted_data = sales_data_path.sort_values(by='total_sales', ascending= False)
  return sales_sorted_data

#find_top_selling_products(sales_sorted_data)
```

----- End of Analysis - 1 ------


# Analysis Sales Data - 2

## Objective

In a shopping mart scenario, we want to simulate product prices and predict future sales based on price changes. We'll use NumPy for random price generation and pandas for data manipulation and analysis

### Data Details

Product Data (CSV):
- Product ID: Unique identifier for each product
- Product Name: Name of the product
Historical Sales Data (CSV):
- Date (format: YYYY-MM-DD)
- Product ID: Reference to product in product data
- Quantity Sold: Number of units sold on that day

### Steps to follow :

- Import pandas and numpy

``` 
import pandas as pd
import numpy as np
```

- load_product_data(filename):
This function loads the product data CSV file into a pandas DataFrame.

It assumes the CSV has a column named "Product ID" (modify if different).

Optional: It can be extended to include a "Product Name" column if available.



```
import pandas as pd

def load_data(sales_c3):
  sales_data_c3 = ("/content/drive/MyDrive/Python_Project/sales_data_c3.csv")
  sales_c3 = pd.read_csv(sales_data_c3)
  return sales_c3

# load_data(sales_c3)

```

- load_sales_data(filename):
This function loads the historical sales data CSV file into a pandas DataFrame.

It assumes the CSV has columns named "Date", "Product ID", and "Quantity Sold" (modify if different).

``` 
import pandas as pd

product_data_1 = ("/content/drive/MyDrive/Python_Project/product_data.csv")
Product1 = pd.read_csv(product_data_1 )

# Product1
  ```

- simulate_prices(product_data, max_price):
This function takes the product data DataFrame, a maximum price as input.

It uses NumPy's random.randint function to generate random initial prices for each product within the given range.

Here the min value should be equal to old_proce value from product_Data

It creates a “new_Price" column in the product data DataFrame with these simulated prices.

It's important to use .copy() to avoid modifying the original product data. This ensures you don't overwrite the actual product data with simulated prices.

```
#simulate_prices(product_data, max_price)

product_data = Product1.copy()
min_prices = product_data['Old_price']
max_price = 520
product_data['New Price'] = [np.random.randint(min_price, max_price+1) for min_price in min_prices]

# print(product_data.head(3))
```
- Output
  
|Product ID | Product Name | Old_price  New |Price|
|-----------|--------------|----------------|-----|
|   1001   | T-Shirt (White) | 200  |  467 |
|  1002    |   Jeans (Blue)  | 250  |  468 |
|   1003  |Sweatshirt (Gray) | 500  |  516 |

- predict_sales(sales_data,product_data):
This function takes historical sales data, and product data.

Fetches the new_cost and old_cost columns which will be respective prices multiplied by quantity.

Return the difference of the total sales with old prices and newprice.

```
#predict_sales(sales_data,product_data):
# Merge sales data with product data to get prices
merged_data = sales_c3.merge(product_data, on='Product ID')

# Calculate total sales with old prices
merged_data['Old Cost'] = merged_data['Quantity'] * merged_data['Old_price']

# Calculate total sales with new prices
merged_data['New Cost'] = merged_data['Quantity'] * merged_data['New Price']

# Calculate the difference in total sales
total_old_sales = merged_data['Old Cost']
total_new_sales = merged_data['New Cost']

merged_data['diff_in_sales'] = total_new_sales - total_old_sales
# merged_data

```

----- End of Code ------

Thank you
