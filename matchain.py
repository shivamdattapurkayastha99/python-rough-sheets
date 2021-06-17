import sys
def matchain(p,i,j):
    if i==j:
        return 0
    min=sys.maxsize
    for k in range(i,j):
        count=matchain(p,i,k)+matchain(p,k+1,j)+p[i-1]*p[k]*p[j]
        if count<min:
            min=count
    return min
if __name__ == "__main__":
    n=int(input("Enter the no of matrices"))
    arr=[int(input("Enter the order of matrices"))for i in range(n)]
    print(f"Minimum no of matrix multiplications is {matchain(arr,1,n-1)}")
