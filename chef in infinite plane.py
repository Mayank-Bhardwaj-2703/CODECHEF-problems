from collections import Counter
#it will count no. of duplicates available in the list and return in form of dictionary with the element and its count as the key.

for _ in range(int(input())):
  
    n=int(input())
    l=list(map(int, input().split()))
    c=0
    m=Counter(l)
    for i in set(l):
        if m[i]>i-1:
            c=c+i-1
        elif m[i]<i-1:
            c=c+m[i]
        elif m[i]==i-1:
            c=c+i-1
    print(c)
