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

# products[0][0]  # procdutcs [] 裡的第 0 個 跟[] 裡面 [] 的第 0 個

for p in products:
    print(p[0], '的價格是', p[1])
    

with open('products.csv', 'w', encoding = 'utf-8') as f:  # with 有 close 的意思，使用完檔案之後就會 close
    f.write('商品,價格\n') 
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')