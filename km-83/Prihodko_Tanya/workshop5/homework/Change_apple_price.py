import plotly
import plotly.graph_objs as go
from data_progr import dataset
a=dataset.keys()
dates=[]
price=[]

for person in dataset:
    for date in dataset[person]:
        if "apple" in dataset[person][date]:
            dates.append(date)
            price.append(dataset[person][date]['apple']["price"])

print(dates)

print(price)

data = go.Scatter(x=dates, y=price)
plotly.offline.plot([data], filename='apple.html')