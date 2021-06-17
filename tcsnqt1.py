# max distance marathon runner
R=[]
num=input("Enter the distances covered by racers press q to exit")
while num!='q':
    R.append(float(num))
    num=input()
result=sorted(R)
for i in result:
    if i<0:
        print("Invalid Input")
        break
print(result[-4:-7:-1])