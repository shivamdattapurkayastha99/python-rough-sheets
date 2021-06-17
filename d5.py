# radix sort
def countingsort(a,exp1):
    n=len(a)
    output=[0]*n
    count=[0]*(10)
    for i in range(0,n):
        index=(a[i]//exp1)
        count[int(index%10)]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i=n-1
    while i>=0:
        index=(a[i]/exp1)
        output[count[int(index%10)]-1]=a[i]
        count[int(index%10)]-=1
        i-=1
    i=0
    for i in range(0,len(a)):
        a[i]=output[i]
def radixsort(a):
    max1=max(a)
    exp=1
    while max1/exp>0:
        countingsort(a,exp)
        exp*=10
a=[5,4,3,2,1]
radixsort(a)
for i in range(len(a)):
    print(a[i])
      


