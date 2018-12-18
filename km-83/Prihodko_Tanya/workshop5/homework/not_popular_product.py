from data_progr import *
from buy_all import *
count=100

prod=""
for i in set_prod:
    if count>=all_product.count(i):
        count=all_product.count(i)
        prod=i
for j in set_prod:
    if (count==all_product.count(j)) and(j!=prod):
        print("prod:",j)
print("prod:",prod)