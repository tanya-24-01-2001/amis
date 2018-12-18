from data_progr import dataset,list_val

all_people=[]
for i in range(len(list_val)):
    all_people.append(list_val[i][0])
# print(all_people)
set_peop=list(set(all_people))

all_product=[]
for i in range(len(list_val)):
    all_product.append(list_val[i][2])
# print(all_product)
set_prod=list(set(all_product))
max_people=len(set_peop)
# print(max_people)
for prod in set_prod:
    if all_product.count(prod)>max_people:
        print(prod)


