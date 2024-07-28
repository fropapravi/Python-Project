
# Analysis Sales Data - 1 (Using Python)

This program analyzes sales data to identify trends and patterns.

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


----- End of Code ------

Thank you
