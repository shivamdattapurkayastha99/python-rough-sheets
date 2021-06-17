# largest possible even no from a string
import re
string=input()
digits=list(set(re.findall("\d",string)))
digits.sort()
digits.reverse()
num=int(''.join(digits))
if num%2==0:
    print(num)
else:
    length=len(digits)
    for i in range(length-1,0,-1):
        if (int(digits[i]))%2==0:
            d=digits[i]
            digits.remove(d)
            digits.insert(length-1,d)
            even_num=int(''.join(digits))
            print(even_num)
            break
    else:
        print('-1')
            
