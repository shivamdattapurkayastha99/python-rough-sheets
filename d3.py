def shellsort(a):
    n=len(a)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=a[i]
            j=i
            while j>=gap and a[j-gap]>temp:
                a[j]=a[j-gap]
                j-=gap
            a[j]=temp
        gap//=2
a=[5,4,3,2,1]
n=len(a)
print("array before sorting")
for i in range(n):
    print(a[i])
shellsort(a)
print("array after sorting")
for i in range(n):
    print(a[i])



        