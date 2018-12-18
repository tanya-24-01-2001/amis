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

        data = go.Scatter(x=date, y=tons)
        plotly.offline.plot([data], filename='apple.html')





except IOError as io_error:
    print("Error with file",io_error.errno,io_error.strerror)
except ValueError as v_error:
    print("Error in line",current_line,v_error)
