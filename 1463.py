#기존 오답코드 (bfs느낌내서 풀려고 시도함) - 시간초과
#입력값으로부터 모든 경우의수를 덱(큐)에 넣어서 1이나올때까지 반복

import sys,collections
input=sys.stdin.readline
n=int(input())
l=collections.deque()
l.append([n,0])
visited=[]
while True:
    k,count=l.popleft()
    if k in visited:
        continue
    else:
        visited.append([k,count+1])
    if k==1:
        print(count)
        break
    l.append([k-1,count+1])
    if k%3==0 and k%2==0:
        l.append([min(k//3,k//2),count+1])
        continue
    if k%3==0:
        l.append([k//3,count+1])
    if k%2==0:
        l.append([k//2,count+1]) 

#BFS     --     122252 mb   /  148 ms
import sys,collections
input=sys.stdin.readline
n=int(input())
l=collections.deque()
visited=[0]*(n+1)
while l:
    k,count=l.popleft()
    if k==1:
        break
    if k%3==0 and visited[c//3]:
        l.append(k//3)
    if k%2==0 and visited[c//2]:
        l.append(k//2)
    if visited[k-1]==0:
        l.append(k-1)
print(visited[1])

# DP_ BottomUp 풀이   --   124244 mb  /  176 ms
# 1부터 시작해서 n까지 올라가는 방법
import sys,collections
input=sys.stdin.readline
n=int(input())
visited=[0]*(n+1)
for i in range(2,n+1):
    visited[i]=visited[i-1]+1
    if i%3==0:
        visited[i]=min(visited[i],visited[i//3]+1)
    if i%2==0:
        visited[i]=min(visited[i],visited[i//2]+1)
print(visited[n])

