products = [
    {'id':101,'name':'Redmi','price':12000},
    {'id':102,'name':'Apple','price':82000},
    {'id':103,'name':'Samsung','price':52000},
    {'id':104,'name':'Apple','price':65000},
    {'id':105,'name':'Redmi','price':15000},
    {'id':106,'name':'Nokia','price':18000},
    {'id':107,'name':'Vivo','price':20000},
    {'id':108,'name':'Apple','price':100000},
    ]

#for p in products:
#    print(p['price'])

sort_by_price = sorted(products, key=lambda p : p['price'])
#print("Sorted data",sort_by_price)
for data in sort_by_price:
    print(data)
print("------------------------------------------")
filter_by_price = list(filter(lambda p : p['price'] > 25000, products))
for data in filter_by_price:
    print(data)
