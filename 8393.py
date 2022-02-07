# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
total = 0
for i in range(1,int(input())+1):
    total  += i
print(total)

# short coding
n = int(input())
print(n*(n+1)//2)
