#  напишите программу, которая принимает на вход число N
# и выдает набор произведений от 1 до N

n = int(input())
f = 1
for i in range(2,n+1):
    f*=i
print(f)

n = int(input())
f = 1
while n>1:
    f*=n
    n=n-1
print(f)
