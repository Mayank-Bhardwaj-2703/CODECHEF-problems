def function():
    a=[]
    a=list(map(int,input().split()))
    water=0
    for i in a:
        if i>0:
            water+=i
        elif i==0:
            if water<d:
                water=0
            else:
                water-=d
        
        if water>h:
            print('YES')
            break;
    if water<=h:
        print('NO')
    
  

for _ in range(int(input())):
    n,d,h=map(int,input().split())
    
    function()        
        
      
#i have created the function to save the time complexity. Local variables declaration takes less time to commit then the global variables.
# Hence creating functions reduces the time complexity.
