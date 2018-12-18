from data_progr import dataset
print("What do you want to add?")
print("if parson-enter p")
print("if data-enter-d")
print("if product-enter pr")
ans=input("Your answer :")
def AddPerson(dataset,name,date,product,quantity,price):
    if not(name in dataset):
        dataset[name] = {date: {product: {'quantity': quantity,'price': price}}}
    else:
        print("this name is in the dictionary")
def AddData(dataset,name,date,product,quantity,price):
    if not(date in dataset[date]):
        dataset[name][date] = {product: {'quantity': quantity,
                                     'price': price}}
    else:
        print("this date is in the dictionary")
def AddProduct(dataset,name,date,product,quantity,price):
    if not(dataset[name][date]):
        dataset[name][date][product] = {'quantity': quantity,
                                    'price': price}
    else:
        print("this product is in the dictionary")
name=input("name :")
date=input("date :")
product=input("product :")
quantity=input("quantity:")
price=input("price")
if ans=="p":
    AddPerson(dataset, name, date, product, quantity, price)
elif ans=="d":
    AddData(dataset, name, date, product, quantity, price)
elif ans=="pr":
    AddProduct(dataset, name, date, product, quantity, price)
else:
    print("enter corect data")
print(dataset)