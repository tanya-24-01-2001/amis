import plotly
import plotly.graph_objs as go
from plotly import tools
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
        header=file.readline().rstrip()
        header_nice=[colum.strip().upper() for colum in header.split('\t')]
        print(header_nice)


        datset = dict()
        ton=[]
        dates=[]
        file.readline()
        for line in file:
            colums = line.split("\t")

            ReportPeriod = colums[1]
            AirCargoTons = colums[5]
            ton.append(AirCargoTons)
            dates.append(ReportPeriod)
            #print(colums)

        set_data=set(dates)
        print(set_data)
        count_date=[]
        for i in list(set_data):
            count_date.append(dates.count(i))
        print(count_date)
        sum=0
        tons=[]
        for j in count_date:
            list=ton[:j:]
            sum=sum_recurs(list,sum)
            tons.append(sum)
            ton=ton[j::]
        print(tons)
        print(set_data)
        date=[]
        for i in set_data:
            date.append(i)

        data1 = go.Scatter(x=date, y=tons)


except IOError as io_error:
    print("Error with file",io_error.errno,io_error.strerror)
except ValueError as v_error:
    print("Error in line",current_line,v_error)




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

except IOError as io_error:
    print("Error with file", io_error.errno, io_error.strerror)
except ValueError as v_error:
    print("Error in line", current_line, v_error)





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

        data3= go.Bar(x=['Freight','Mail'], y=[sum_recurs(ton_f,0),sum_recurs(ton_m,0)])

except IOError as io_error:
    print("Error with file", io_error.errno, io_error.strerror)
except ValueError as v_error:
    print("Error in line", current_line, v_error)



fig = tools.make_subplots(rows=1, cols=3)

fig.append_trace(data1, 1, 1)

fig.append_trace(trace, 1, 2)
fig.append_trace(data3, 1, 3)

plotly.offline.plot(fig, filename='plotly.html')