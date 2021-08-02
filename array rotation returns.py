for u in range(int(input())):
    n = int(input())
    x = [int(w) for w in input().split()]
    y = [int(w) for w in input().split()]
    
    z = []
    for i in range(n):
        if(y.count(abs(n-x[0]+i)) > 0):
            z.append(abs(n-x[0]+i))
            
        if(2*n-x[0]+i <= 2*n):
            if(y.count(abs(2*n-x[0]+i))):
                z.append(abs(2*n-x[0]+i))
                
        if(len(z)):
            break
        
    p = [0]*(len(z))
    t = 0
    while(t<len(z)):
        for i in range(n):
            if(y[i] == z[t]):
                p[t] = i
                
        t += 1
    
    q = []
    t = 0
    while(t<len(z)):
        a = []
        s = p[t]
        
        for i in range(s, n):
            a.append(y[i])
        for i in range(s):
            a.append(y[i])
            
        q.append(a)
        t += 1
        
    ans = [[0 for j in range(n)] for i in range(len(z))]
    t = 0
    while(t < len(z)):
        for i in range(n):
            ans[t][i] = (x[i] + q[t][i])%n
            
        t += 1
        
    ans = sorted(ans)
    print(*ans[0])
