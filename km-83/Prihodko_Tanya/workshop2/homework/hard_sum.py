list = [1, [2, [3], [1, 2]], 4]


def sum_1_for(list):
    sum = 0
    for i in range(0, len(list)):
        if type(list[i]) == type(3):
            sum = sum + list[i]
        else:
            for j in range(0, len(list[i])):
                if type(list[i][j]) == int:
                    sum = sum + list[i][j]
                else:
                    for k in range(0, len(list[i][j])):
                        if type(list[i][j][k]) == int:
                            sum = sum + list[i][j][k]
    return sum


def sum_1_while(list):
    sum = 0
    i = 0
    while i != (len(list)):
        if type(list[i]) == type(3):
            sum = sum + list[i]
        else:
            j = 0
            while j != (len(list[i])):
                if type(list[i][j]) == type(3):
                    sum = sum + list[i][j]
                else:
                    k = 0
                    while k != (len(list[i][j])):
                        if type(list[i][j][k]) == type(3):
                            sum = sum + list[i][j][k]
                        k = k + 1
                j = j + 1
        i = i + 1
    return sum


def sum_1_recurs(list, sum):
    if len(list) == 0:
        return sum
    else:
        if type(list[0]) == type(3):
            sum = sum + list[0]
        else:
            sum = sum_1_recurs(list[0], sum)
        sum = sum_1_recurs(list[1::], sum)
    return sum


def sum_1_recurs_unchanged(list, sum, i):
    if len(list) == 0 or i == len(list):
        return sum
    if type(list[i]) == type(3):
        element = list[i]
        sum = sum + element
        sum = sum_1_recurs_unchanged(list, sum, i + 1)
    else:
        sum = sum_1_recurs_unchanged(list[i], sum, 0)
        sum = sum_1_recurs_unchanged(list, sum, i + 1)
    return sum


print('sum_for =', sum_1_for(list))
print('sum_while =', sum_1_while(list))
print('sum_recurs =', sum_1_recurs(list, 0))
print('sum_1_recurs_unchanged =', sum_1_recurs_unchanged(list, 0, 0))

