# cook your dish here
r1,r2=map(int,input().split())
d1,d2=map(int,input().split())
print("Dominator" if r1+d1>r2+d2 else "Everule")