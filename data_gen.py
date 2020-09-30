#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:53:21 2020

@author: mistageek
"""
import pandas as pd
import numpy as np
import random
import calendar

from gen_address import gen_address
from gen_date import gen_date

# Products with Price and Weights how common they are bought
products = {
    # 'Product': [Price, Weight]
    "Nokia VI" : [15999, 10],
    "Samsung Type-C Charger": [3000, 30],
    "Generic Type-C Charger": [1500, 30],
    "Samsung Type-B Charger" : [1000, 35],
    "Google Pixel 4" : [25567, 10],
    "Samsung Note 5" : [53000, 10],
    "Apple iPhone 7" : [56987, 10],
    "Huawei Mate 10" :[39999, 10],
    "Xiaomi Pro" : [26500, 10],
    "Oppo Neo 6" : [35600, 12],
    "LG Xmax Pro" : [27800, 12],
    "Motorola Matte 12" : [19100, 7],
    "Mobicel T" : [10200, 5],
    "Lenovo Note" : [18500, 7],
    "Tecno Camon" : [12000, 22],
    "Infinix 7" : [14985, 22],
    "Vivo" : [24145, 5],
    "Blackberry" : [26000, 5],
    "OnePlus" : [27600, 7],
    "Asus" : [20000, 7],
    "Xtigi" : [7000, 16],
    "Cubot" : [8000, 18],
    "Sony" : [41000, 10],
    "HTC" : [13000, 8],
    "Alcatel" : [12400, 5],
    "Wiko" : [5000, 5],
    "itel" : [4000, 8],
    "Sony Flatscreen TV" : [100000, 5],
    "Macbook Pro Laptop" : [100500, 3],
    "Thinkpad Laptop": [47000, 7],
    "HP Laptop" : [53000, 7],
    "iMac Desktop" : [400000, 2],
    "Wired Earphones" : [700, 35],
    "Wireless Earphones" : [2000, 28],
    "Wired Headphones" : [5000, 25],
    "Wireless Headphones" : [10000, 20],
    "Fast Charge Cable" : [4000, 25],
    "Apple ipod": [20000, 10],
    "42in 4K Monitor" : [55000, 11],
    "20in Monitor" : [23000, 10],
    "Nikon Camera" : [70000, 2],
    "Canon Camera" : [75000, 2],
}

if __name__ == "__main__":
    # Function to aggregate data in a row format
    def row_data(order_id, product, o_date, address):
        price = products[product][0]
        quantity_o = np.random.geometric(p=1.0-(1.0/price), size=1)[0]
        
        return [order_id, product, quantity_o, price, o_date, address]
    
    # Loop through the Products Dictionary and obtain the product names
    product_list = [product for product in products]
    
    # Loop through the Products Dictionary and obtain the weights
    weight = [products[product][1] for product in products]
    
    # Column names for the dataframes
    columns = ['Order ID', 'Product','Quantity', 'Price', 'Order Date', 'Purchase Address']
    
    #Create an empty DataFrame to be used as template
    df = pd.DataFrame(columns=columns)
    
    order_id = 117860
    
    
    for month_v in range(1, 13):
        if month_v <= 10:
            order_amount = int(np.random.normal(loc=1500, scale=300))
        if month_v == 11:
            order_amount = int(np.random.normal(loc=2500, scale=300))
        if month_v == 12:
            order_amount = int(np.random.normal(loc=3100, scale=300))
            
        i = 0
        while order_amount > 0:
            address = gen_address()
            o_date = gen_date(month_v)
            product = random.choices(product_list, weights = weight)[0]
            
            df.loc[i] = row_data(order_id, product, o_date, address)
            i+= 1
            
            if product == "Apple iPhone 7":
                if random.random() < 0.15:
                    df.loc[i] = row_data(order_id, "Apple ipod", o_date, address)
                    i +=1
                    df.loc[i] = row_data(order_id, "Fast Charge Cable", o_date, address)
                    i +=1
                if random.random() < 0.05:
                    df.loc[i] = row_data(order_id, "Fast Charge Cable", o_date, address)
                    i +=1
                if random.random() < 0.07:
                    df.loc[i] = row_data(order_id, "Apple ipod", o_date, address)
                    i +=1
            elif product == "Nokia VI" or product =="Samsung Note 5" or product == "Google Pixel 4" or product == "Huawei Mate 10" or product == "Motorola Matte 12" or product == "Xiaomi Pro" or product == "Oppo Neo 6" or product == "LG Xmax Pro":
                if random.random() < 0.15:
                    df.loc[i] = row_data(order_id, "Samsung Type-C Charger", o_date, address)
                    i +=1
                    df.loc[i] = row_data(order_id, "Wireless Headphones", o_date, address)
                    i +=1
                if random.random() < 0.05:
                    df.loc[i] = row_data(order_id, "Fast Charge Cable", o_date, address)
                    i +=1
                if random.random() < 0.07:
                    df.loc[i] = row_data(order_id, "Wired Headphones", o_date, address)
                    i +=1
            elif product == "Mobicel T" or product =="Lenovo Note" or product == "Tecno Camon" or product == "Infinix 7" or product == "Vivo" or product == "Sony" or product == "Blackberry" or product == "OnePlus" or product == "Asus" or product == "Xtigi" or product == "Cubot" or product =="Alcatel" or product == "Wiko" or product == "HTC" or product == "itel":
                if random.random() < 0.15:
                    df.loc[i] = row_data(order_id, "Samsung Type-B Charger", o_date, address)
                    i +=1
                    df.loc[i] = row_data(order_id, "Wired Earphones", o_date, address)
                    i +=1
                if random.random() < 0.05:
                    df.loc[i] = row_data(order_id, "Fast Charge Cable", o_date, address)
                    i +=1
                if random.random() < 0.07:
                    df.loc[i] = row_data(order_id, "Wireless Earphones", o_date, address)
                    i +=1
            order_id += 1
            order_amount -= 1
        
        month_name = calendar.month_name[month_v]
        print(month_name + " Finished!!")
        df.to_csv(f"{month_name}_data.csv")
        