"""
Потрібно обчислити, скільки банок фарби потрібно, щоб пофарбувати поверхню бака циліндричної форми.
Пофарбувати треба і зовні, і зсередини. Користувач вводить діаметр і висоту бака,
а також, яку площу можна забарвити однієї банкою фарби.

"""
def input_int_data(text):           #the program that enters the integer data
    a=int(input(text))
    return a


def print_data(text):               #program that displays data
    print(text)

def number_of_cans(S,d,h):
    r=d/2               #radius
    Sb=2*3.14*r*h       #area of the lateral surface
    So=3.14*r*r         #площа основи
    Sp=2*(2*So+Sb )     #area of the cylinder on both sides
    N=Sp/S              #the number of cans of paint that will be needed
    if N -N//1>0 :
        N=(N+1)//1
    return N

S=input_int_data('S=')
d=input_int_data('d=')
h=input_int_data('h=')

N=number_of_cans(S,d,h)
print_data(N)