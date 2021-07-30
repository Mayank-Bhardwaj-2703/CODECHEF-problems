for _ in range(int(input())):
    n=int(input())
    A=list(map(int, input().split()))
    temp=0
    x=A[0]
    for i in range(n):
        temp=temp|(A[i]^x)
    print(x,temp)
