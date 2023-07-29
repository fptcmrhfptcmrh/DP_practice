#백준 11726번 [2xn 타일링]
#n개일때는 n-1개의 경우에 | 를 붙이거나 n-2개의 경우에 = 를 붙이면된다.
#따라서 n개일때 경우의수는 n-1개의 경우의수와 n-2개의 경우의수를 더하면 된다.
import sys
input=sys.stdin.readline
n=int(input())
l=[0,1,2]+[0]*(n-1)
if n==1: print(1)
elif n==2: print(2)
else:
    for i in range(3,n+1):
        l[i]=(l[i-1]+l[i-2])%10007
    print(l[n]%10007)
