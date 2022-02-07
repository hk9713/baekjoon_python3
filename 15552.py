# 첫 줄에 테스트케이스의 개수 T가 주어진다. 
# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.
import sys
for i in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)

#short coding1
input()
for i in sys.stdin:
    print(sum(map(int,i.split())))

#short coding2
for N in [*open(0)][1:]:print(sum(map(int,N.split())))