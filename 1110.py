'''
n = int(input())
a = list(map(int,str(n)))
if len(a) != 2:
    a.insert(0,0)
hap = sum(a)
b = list(map(int,str(hap)))
if len(b) != 2:
    b.insert(0,0)
num=[]
num.append(a[1])
num.append(b[1]) 
'''
n= int(input())
num = n
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a+b) % 10
    num = (b*10)+c

    cnt = cnt+1
    if(num == n):
        break
print(cnt)
