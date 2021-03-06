import sys
sys.stdin = open("data/in7.txt", "rt")

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

#강의 설명 듣고 내 풀이
def Count(len) :
    cnt = 0
    num = 0
    for x in a :
        if num + x > len :
            cnt += 1
            num = x
        else:
            num += x
    if num >= 1 :
        cnt += 1
    print(cnt)
    return cnt  
    
lt = 1
rt = sum(a)
while lt <= rt :
    mid  = (lt + rt) // 2 #23, 11
    if Count(mid) <= M : #3
        res = mid
        rt = mid - 1
    else :
        lt = mid + 1
print(res)

#강의 풀이 + 반례 수정
def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m=map(int, input().split())
Music=list(map(int, input().split()))
# 리스트 중 가장 큰 노래
maxx=max(Music)
lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    # 용량이 가장 큰 노래보다 mid는 크거나 같아야 한다. 
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1


