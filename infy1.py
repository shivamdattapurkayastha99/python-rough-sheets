# password generator problem
inp=input()
list_input=[]
fstr=''
list_input=inp.split(',')
for i in list_input:
    temp=i.split(':')
    name=temp[0]
    number=temp[1]
    length=len(name)
    max=0
    for digit in number:
        if int(digit)<=length:
            if max<int(digit):
                max=int(digit)
    if max==0:
        fstr+='X'
    else:
        fstr+=name[max-1]
print(fstr)