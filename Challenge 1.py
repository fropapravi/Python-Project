# Challenge 2

from google.colab import drive
drive.mount("/content/drive")

#Analyzing Sales Data
import pandas as pd
def load_data(sales_data_path):
  sales_data_path = ("/content/drive/MyDrive/Python_Project/sales_data.csv")
  sales = pd.read_csv(sales_data_path)
  return sales

# calculate_total_sales(data)
def calculate_total_sales(data):
  sales_data_path['total_sales'] = sales_data_path["Quantity"] * sales_data_path["Price"]
  return sales_data_path

#find_top_selling_products(data, num_products=5)

import numpy as np
def find_top_selling_products(data, num_products=5):
  sales_data_path['total_sales'] = sales_data_path["Quantity"] * sales_data_path["Price"]
  sales_sorted_data = sales_data_path.sort_values(by='total_sales', ascending= False)
  return sales_sorted_data

#find_top_selling_products(sales_sorted_data)
