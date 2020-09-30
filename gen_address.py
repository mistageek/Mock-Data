#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:29:48 2020

@author: mistageek
"""
import random

def gen_address():
    street_names = ["Main", "1st", "2nd", "3rd", "U. Highway", "Ken. Avenue", "T Mboya", "Valley Rd", "H. Sellasie", "Ring Rd"]
    cities = ["Nairobi", "Mombasa", "Eldoret", "Kisumu", "Nakuru", "Thika", "Kisii", "Machakos", "Meru", "Naivasha"]
    weights = [9, 7, 4, 6, 5, 4, 8, 6, 2, 0.5]
    
    street = random.choices(street_names)[0]
    index_cities = random.choices(range(len(cities)), weights=weights)[0]
    
    return f"{random.randint(1, 999)} {street} st., {cities[index_cities]}"
