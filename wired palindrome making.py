t=int(input())
for i in range(t):
    c=0
    n=int(input())
    e=map(int,input().split())
    for j in e:
        if j%2!=0:
            c+=1
    print(c//2)
        
