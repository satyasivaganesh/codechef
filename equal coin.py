t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x%2==0 and y%2==0:
        print("yes")
    elif x%2==0 and y%2!=0 and x!=0:
        print("yes")
    else:
        print("no")
        
