t=int(input())
for i in range(t):
    x,y,a,b,k=map(int,input().split())
    p=k*a+x
    d=k*b+y
    if p<d:
        print("PETROL")
    elif p>d:
        print("DIESEL")
    else:
        print("SAME PRICE")
