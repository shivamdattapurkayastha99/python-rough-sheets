# armstrong no
def armstrong(n):
    n1=n
    s=0
    while n!=0:
        d=n%10
        s=s+d**3
        n//=10
    if s==n1:
        return True
    else:
        return False
if __name__ == "__main__":
   n=int(input("Enter the number to checked for armstrong"))
   if armstrong(n)==True:
       print("it is armstrong")
   else:
        print("Not armstrong")

