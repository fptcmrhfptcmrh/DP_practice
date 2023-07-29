#백준 9095번 [1,2,3 더하기]
#값을 더해서 n을 만드려면 n-1의 값에 1을 더한다 / n-2의 값에 2를 더한다 / n-3의 값에 3을 더한다 이 경우로 나뉘게 된다.
#따라서 방법의수는 n-1의 수, n-2의 수, n-3의 수를 모두 더하면 된다.

import sys
input=sys.stdin.readline
l=[0,1,2,4]+[0]*8
for i in range(4,11):
  l[i]+=l[i-1]+l[i-2]+l[i-3]
n=int(input())
for _ in range(n):
  k=int(input())
  print(l[k])
