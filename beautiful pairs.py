
def beautiful_pair(a,b):
    return (a-b)/a

def main_func():
    count=0
    a=list(map(int,input().split()))
    
    for i in range(n):
        for j in range(n):
            if i!=j and beautiful_pair(a[i],a[j])<beautiful_pair(a[j],a[i]):
                count+=1
                
    print(count*2)

for _ in range(int(input())):

    n=int(input())
    main_func()
                
    
