for _ in range(int(input())):
    n,m,q=map(int,input().split())
    
    l=[]
    flag=1
    for _ in range(q):
        c,i=input().split()
        i=int(i)
        if(c=='-' and (i not in l)):
            flag=0
            continue
        if(c=='+' and (len(l)>=m)):
            flag=0
            continue
        if(c=='+' and (i not in l) and (len(l)<m)):
            l.append(i)
        if(c=='-' and (i in l)):
            l.remove(i)
    if flag==1:
        print('Consistent')
    else:
        print('Inconsistent')
           
