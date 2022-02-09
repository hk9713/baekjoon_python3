# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    print("Case #%d: %d" % (i+1,a+b))

# short coding
for i in range(int(input())):
    print("Case #%d: %d" % (i+1,sum(map(int,input().split()))))