def isprime(n):
    flag=1
    for i in range(2,n//2+1):
        if n%i==0:
            flag=0
            break
    return flag
def checksum(a,b):
    return isprime(a) and isprime(b) and isprime(a+b)
            
    # print(c)
if __name__ == "__main__":
    c=0
    limit=int(input("Enter the upper range of the limit"))
    for i in range(3,limit):
        for j in range(2,i):
            
            if checksum(i,j):
                c+=1
    print(c//2)
