
from data_progr import dataset
prod=[]
price=[]
for person in dataset:
    for date in  dataset[person]:
        for product in dataset[person][date]:
            prod.append(product)
            price.append(float(dataset[person][date][product]['price']))
print(prod)
print(price)
maximum=price[0]
for i in range(len(price)):
    if maximum<price[i]:
        maximum=price[i]
# print(maximum)
index=price.index(maximum)

print(prod[index])