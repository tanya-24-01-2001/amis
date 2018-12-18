from data_progr import *
from buy_all import *
count=0
prod=""
for i in set_prod:
    if count<all_product.count(i):
        count=all_product.count(i)
        prod=i
print("prod:",prod)