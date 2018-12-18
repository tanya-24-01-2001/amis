import plotly
import plotly.graph_objs as go

def sum_recurs(list,sum):
    if len(list)==0:
        return sum
    else:
        sum=sum+int(list[0])
        sum=sum_recurs(list[1::],sum)
        return sum


try:
    current_line=0
    with open("data_.txt",mode="r",encoding="utf-8") as file:
        datset = dict()
        ton_i=[]
        ton_d=[]
        tons=[]
        i_d=[]
        file.readline()
        for line in file:
            colums = line.split("\t")


            tons.append(colums[5])
            i_d.append(colums[3])
        # print(i_d)
        for i in range(len(tons)):
            if i_d[i]=='Domestic':
                ton_d.append(int(tons[i]))
            if i_d[i]=='International':
                ton_i.append(int(tons[i]))
        # print(ton_d)
        # print(ton_i)

        trace = go.Pie(labels=["International","Domestic"], values=[sum_recurs(ton_i,0),sum_recurs(ton_d,0)])

        plotly.offline.plot([trace], filename='product_user.html')
except IOError as io_error:
    print("Error with file", io_error.errno, io_error.strerror)
except ValueError as v_error:
    print("Error in line", current_line, v_error)
