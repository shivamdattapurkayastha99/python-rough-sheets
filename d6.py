# to add two polynomials
def add(a,b,m,n):
    size=max(m,n)
    sum=[0 for i in range(size)]
    for i in range(0,m,1):
        sum[i]=a[i]
    for i in range(n):
        sum[i]+=b[i]
    return sum
def printpoly(poly,n):
    for i in range(n):
        print(poly[i],end="")
        if i!=0:
            print("x^",i,end="")
        if i!=n-1:
            print("+",end="")
if __name__ == "__main__":
    a=[5,0,10,6]
    b=[1,2,4]
    m=len(a)
    n=len(b)
    print("first polynomial")
    printpoly(a,m)
    print("second polynomial")
    printpoly(b,n)
    sum=add(a,b,m,n)
    size=max(m,n)
    print("sum polynomial is ")
    printpoly(sum,size)


