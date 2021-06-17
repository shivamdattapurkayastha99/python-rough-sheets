# bracket validator
def validator(string):
    stack=[]
    count=0
    for b in string:
        if b=='[' or b=='{' or b=='(':
            stack.append(b)
            count+=1
            continue
        if len(stack)==0:
            return count+1
        x=stack.pop()
        if b==']' and x=='[':
            count+=1
        elif b=='}' and x=='{':
            count+=1
        elif b==')' and x=='(':
            count+=1
        else:
            return count+1
    if len(stack)==0:
        return 0
    else:
        return count+1
string=input()
print(validator(string))