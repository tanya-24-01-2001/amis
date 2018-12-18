file = open('data_text.txt') #Відкриваєм файл

reading=file.read() #читаєм

lines = reading.splitlines()  #розбиваєм на лінії
size=len(lines)
keys=lines[0].split(" ")

list_val=[]
for i in range(1,size):
    values=lines[i].split("\t")
    list_val.append(values)

list_val=[]
for i in range(1,size):
    values=lines[i].split("\t")
    list_val.append(values)

print(list_val)
dataset=dict()


for client in list_val:
    name = client[0]
    date = client[1]
    product = client[2]
    quantity = client[3]
    price = client[4]
    if name in dataset:
        if date in dataset[name]:
            if product in dataset[name][date]:
                dataset[name][date][product]['quantity'] += quantity
                dataset[name][date][product]['price'] += price
            else:
                dataset[name][date][product] = {'quantity': quantity,
                                                'price': price}
        else:
            dataset[name][date] = {product: {'quantity': quantity,
                                             'price': price}}
    else:
        dataset[name] = {date: {product: {'quantity': quantity,
                                          'price': price}}}
print(dataset)

file.close()


