for _ in range(int(input())):
    n=int(input())
    
    A=list(map(int,input().split()))
    temp2=0
    x=0
    temp=A[0]
    for i in range(n):
        if temp>A[i]:
            temp=A[i]
            
    for i in range(n):
        if temp==A[i]:
            x+=1
    if temp==0:
        print(n-x)
    else:
        for i in range(n):
            if x!=A[i] and ((A[i]-x)<-x):
                temp2=1
                break
        if temp2==1:
            print(n)
        else:
            print(n-x)
        
