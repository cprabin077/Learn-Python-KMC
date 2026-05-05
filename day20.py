# Dictionary Comprehension continue

#  Get all prices below 5 in US dollars
us_price = {
    'milk':2.05,
    'bread':2.6,
    'butter':3.6,
    'mobile':50,
    'television':1000,
    'refrigerator':700
}

#Non-pythonic 
# output = {}
# for k,v in us_price.items():
#     if v<5:
#         output.update({k: v})
# print(output) # {'milk': 2.05, 'bread': 2.6, 'butter': 3.6}

# Pythonic code
# output = {
#     k: v 
#     for k,v in us_price.items() 
#     if v<5}
# print(output) # {'milk': 2.05, 'bread': 2.6, 'butter': 3.6}

# Non-pythonic 
output = {}
for k,v in us_price.items():
    if v<5:
        output.update({k: round(v*1.13*145, 2)})
    else:
        output.update({k: round(v*1.20*145, 2)})
print(output) # {'milk': 335.89, 'bread': 426.01, 'butter': 589.86, 'mobile': 8700.0, 'television': 174000.0, 'refrigerator': 121800.0}

# Pythonic way
output = { 
    k: (round(v*1.13*145, 2) if v<5 else round(v*1.20*145, 2))
    for k,v in us_price.items() 
    }
print(output) # {'milk': 335.89, 'bread': 426.01, 'butter': 589.86, 'mobile': 8700.0, 'television': 174000.0, 'refrigerator': 121800.0}




