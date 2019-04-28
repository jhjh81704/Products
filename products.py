# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:57:00 2019

@author: user
"""

products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    p = []
#    p.append(name)
#    p.append(price)
#    p = [name, price]
    products.append([name, price])  # 把上面三行程式碼成這一行
print(products)

products[0][0]