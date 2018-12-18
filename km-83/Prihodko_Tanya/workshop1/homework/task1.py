"""
Написати програму, яка аналізує дані про вік і відносить людину до однієї з чотирьох груп:
дошкільник, учень, працівник, пенсіонер. Вік вводиться з клавіатури.

"""

def input_int_data(text):           #the program that enters the integer data
    a=int(input(text))
    return a

def input_data(text):
    a = input(text)
    return a

def print_data(text):               #program that displays data
    print(text)

def which_group(age,w_m):
    if age > 0 and age <= 6 :
        group = " Дошкільник "
    elif age > 6 and age <= 17 :
        group = " Учень "
    elif age > 17 and (((age <= 58.5) and (w_m==1) ) or ((age <= 60) and (w_m==2))):
        group = "Працівник"
    elif  ( (age > 58.5) and (w_m==1) ) or ( (age >60) and (w_m==2)):
        group = "Пенсіонер"
    else :
        group = "Введіть додатнє число"
    return group

w_m=int(input_data("If you are a woman, then enter 1 if the man is the other number :"))
age=input_int_data("enter your ege ")
your_group=which_group(age,w_m)
print_data(your_group)