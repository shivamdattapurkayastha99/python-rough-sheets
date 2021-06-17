def nthugly(n):
    ugly=[0]*n
    ugly[0]=1
    i2=i3=i5=0
    nextmultipleof2=2
    nextmultipleof3=3
    nextmultipleof5=5
    for l in range(1,n):
        ugly[l]=min(nextmultipleof2,nextmultipleof3,nextmultipleof5)
        if ugly[l]==nextmultipleof2:
            i2+=1
            nextmultipleof2=ugly[i2]*2
        if ugly[l]==nextmultipleof3:
            i3+=1
            nextmultipleof3=ugly[i3]*3
        if ugly[l]==nextmultipleof5:
            i5+=1
            nextmultipleof5=ugly[i5]*5
    return ugly[-1]
def main():
    n=150
    print(nthugly(n))
if __name__ == "__main__":
    main()
    
        
        