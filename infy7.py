dictionary=input().split(",")
for obj in dictionary:
    str_obj=obj.split(":")
    string=str_obj[0]
    length=len(string)
    num=str_obj[1]
    sum=0
    for digit in num:
        sum+=(int(digit)**2)
    if sum%2==0:
        s=string[length-2:length]
        print(s+string[0:length-2],end=' ')
    else:
        s=string[0]
        print(string[1:length]+s,end=' ')
