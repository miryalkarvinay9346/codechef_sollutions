# cook your dish here
for _ in range(int(input())):
    r1,r2,r3,r4,r5=map(int,input().split())
    c=0
    if r1>0:
        c+=1
    if r2>0:
        c+=1
    if r3>0:
        c+=1
    if r4>0:
        c+=1
    if r5>0:
        c+=1
    print("YES" if c>=4 else "NO")