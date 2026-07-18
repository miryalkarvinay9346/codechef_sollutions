# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    print("yes" if x*15>=2*y else "NO")