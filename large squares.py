from math import sqrt, floor
def isPerfect(N):
    if (sqrt(N) - floor(sqrt(N)) != 0):
        return False
    return True

def getClosestPerfectSquare(a,N):
    if (isPerfect(N)):
        print(a*int(sqrt(N)))
    else:   
        belowN = -1
        n1 = 0

        n1 = N - 1
        while (True):
            if (isPerfect(n1)):
                belowN = n1
                break
            else:
                n1 -= 1

        print(a*int(sqrt(belowN)))

for _ in range(int(input())):
    n,a=map(int,input().split())
    
    getClosestPerfectSquare(a,n)
