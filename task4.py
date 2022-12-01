# задайте список из n элементов, заполенных числами
# из промежутка [-n,n]. найти произведение элементов на указанных позициях
# ввести с консоли

from random import randint
num = []
for i in range (5):
    num.append(randint(-5,5))
print(num)

def get_num (num):
    count =0
    for element in num:
        count +=1
        return count
print('numbers elements:', get_num (num))

x = int(input('введите позицию первого элемета:'))
y = int(input('введите позицию второго элемета:'))
for i in range(len(num)):
    mult = num[x-1]*num[y-1]
print(f'Mult of elements:{ num[x-1]}*{num[y-1]} =', mult)