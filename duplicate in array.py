def MissingNumber(arr):
    s=((n-2)*(n-1))//2
    t=sum(arr)
    return(t-s)
pass
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=MissingNumber(arr)
print(ans)
