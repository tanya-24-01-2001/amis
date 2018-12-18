import plotly
import plotly.graph_objs as go
from data_progr import dataset
product_user = dict()
for client in dataset:
    for date in dataset[client]:
        for product in dataset[client][date]:
            if product not in product_user:
                product_user[product] = 0

            product_user[product]+=1

data = go.Bar(x=list(product_user.keys() ), y=list(product_user.values()))
plotly.offline.plot([data], filename='product_user.html')