import math

w,h=map(int, input().split())
n,a,b=map(int, input().split())

if (w<a) or (h<b):
    print(-1)
else:
    onePage=(w//a) * (h//b)
    print(math.ceil(n/onePage))