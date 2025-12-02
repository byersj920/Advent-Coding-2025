raw_ID_list = """52-75,1-20,100-200"""
ID_list = raw_ID_list.split(',')

products = []
product_num = 1

for ID in ID_list:
    product = {}
    splitID = ID.split('-')
    
    product["product_num"] = product_num
    product_num += 1
    product["min"] = int(splitID[0])
    product["max"] = int(splitID[1])

    products.append(product)
