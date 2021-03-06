# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:57:00 2019

@author: user
"""

import os # operating system

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 繼續: 直接跳到下一回圈
            name, price = line.strip().split(',')  # strip: remove 最後面的 '\n'
            products.append([name, price])
    return products
        

# 請使用者輸入
def user_input(products):
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
    return products

# products[0][0]  # procdutcs [] 裡的第 0 個 跟[] 裡面 [] 的第 0 個

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])
    
# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:  # with 有 close 的意思，使用完檔案之後就會 close
        f.write('商品,價格\n') 
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 檢查檔案在不在
        print('yeah! 找到檔案了!')
        products = read_file(filename)
    else:
        print('找不到檔案......')

    products = read_file('products.csv')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)
    
main()