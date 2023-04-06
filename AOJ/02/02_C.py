a,b,c = map(int,input().split())
if a>b:
    temp = a
    a = b
    b = temp

if a>c:
    temp = a
    a = c
    c = temp

if b>c:
    temp = b
    b = c
    c = temp

print(a,b,c)