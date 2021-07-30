t=int(input())
count=0
for i in range(t):
    x,y=map(int,input().split())
    
    def gcd(a,b):
        if(b==0):
            return a
        else:
            return gcd(b,a%b)
    if gcd(x,y)>1:
        print('0')
    elif gcd(x,y+1)>1 or gcd(x+1,y)>1:
        print('1')
    else:
        print('2')
