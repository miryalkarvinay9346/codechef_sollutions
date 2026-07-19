# cook your dish here
for _ in range(int(input())):
    x,y,m=map(int,input().split())
    print("YES" if x*m<y else "NO")