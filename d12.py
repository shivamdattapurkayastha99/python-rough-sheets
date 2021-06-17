import math
def maxprimefactors(n):
    maxprime=-1
    while n%2==0:
        maxprime=2
        n/=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            maxprime=i
            n/=i
    if n>2:
        maxprime=n
    return int(maxprime)
n=15
print(maxprimefactors(n))

