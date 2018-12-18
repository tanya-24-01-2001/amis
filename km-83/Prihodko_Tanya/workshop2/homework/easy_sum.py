size=int(input('Enter the size of the list '))
print('Enter the list items ')
list=[int(input()) for element in range(0,size)]
def sum_for(list):
    sum=0
    for i in range (0,len(list)):
        sum=sum+list[i]
    return sum
def sum_while(list):
    sum=0
    j=0
    while j!=(len(list)):
        sum=sum+list[j]
        j=j+1
    return sum
def sum_recurs(list,sum):
    if len(list)==0:
        return sum
    else:
        sum=sum+list[0]
        sum=sum_recurs(list[1::],sum)
        return sum
def sum_recurs_unchanged(list,sum,i):
    if len(list)==0 or i==len(list):
        return sum
    element=list[i]
    sum=sum+element
    sum=sum_recurs_unchanged(list,sum,i+1)
    return sum

print('sum for =',sum_for(list))
print('sum while =',sum_while(list))
print('sum_recurs = ',sum_recurs(list,0))
print('sum_recurs_unchanged =',sum_recurs_unchanged(list,0,0))
