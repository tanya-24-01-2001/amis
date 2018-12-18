import plotly
import plotly.graph_objs as go
from data_progr import dataset
name=list(dataset.keys())
print(name)
spent=[]
spent_pers=0
for person in dataset:
    for date in dataset[person]:
        for product in dataset[person][date]:
            one_prod=float(dataset[person][date][product]['quantity'])*float(dataset[person][date][product]['price'])
        spent_pers=spent_pers+one_prod
    spent.append(spent_pers)
print(name)
print(spent)

data = go.Bar(x=name , y=spent)
plotly.offline.plot([data], filename='user_expenses.html')
