# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    print("Case #%d: %d + %d = %d" % (i+1,a,b,a+b))

# short coding
for i in range(1,int(input())+1): a,b=map(int,input().split());print(f"Case #{i}: {a} + {b} = {a+b}")