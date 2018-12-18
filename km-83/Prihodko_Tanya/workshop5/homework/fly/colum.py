import plotly
import plotly.graph_objs as go

def sum_recurs(list,sum):
    if len(list)==0:
        return sum
    else:
        sum=sum+int(list[0])
        sum=sum_recurs(list[1::],sum)
        return sum

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
        ton_f=[]
        ton_m=[]
        tons=[]
        c_t=[]
        file.readline()
        for line in file:
            colums = line.split("\t")


            tons.append(colums[5])
            c_t.append(colums[4])
        print(c_t)
        for i in range(len(tons)):
            if c_t[i]=='Freight':
                ton_f.append(int(tons[i]))
            if c_t[i]=='Mail':
                ton_m.append(int(tons[i]))
        print(ton_f)
        print(ton_m)

        data= go.Bar(x=['Freight','Mail'], y=[sum_recurs(ton_f,0),sum_recurs(ton_m,0)])

        plotly.offline.plot([data], filename='apple.html')
except IOError as io_error:
    print("Error with file", io_error.errno, io_error.strerror)
except ValueError as v_error:
    print("Error in line", current_line, v_error)
