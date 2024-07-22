#Challenge 2

#shopping mart scenario
import pandas as pd
def load_data(sales_c3):
  sales_data_c3 = ("/content/drive/MyDrive/Python_Project/sales_data_c3.csv")
  sales_c3 = pd.read_csv(sales_data_c3)
  return sales_c3

#simulate_prices(product_data, max_price)
product_data = Product1.copy()
min_prices = product_data['Old_price']
max_price = 520
product_data['New Price'] = [np.random.randint(min_price, max_price+1) for min_price in min_prices]

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
