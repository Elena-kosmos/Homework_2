# задайте список из n чисел последовательности
# (1+1/n)^n  и выведите на экран их сумму
# 6: (2.0; 2,25; 2.37; 2,44; 2,48; 2,52)

n = int(input('введите число:'))
def sequence(n):
    return[round(((1+1/n)**n),2) for n in range (1, n+1)]
print(sequence(n))
print(round(sum(sequence(n))))


  

