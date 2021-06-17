def isoperand(c):
    return c.isdigit()
def evaluateexp(exp):
    stack=[]
    for c in exp:
        if isoperand(c):
            stack.append(int(c))
        else:
            o1=stack.pop()
            o2=stack.pop()
            if c=='+':
                stack.append(o1+o2)
            elif c=='-':
                stack.append(o1-o2)
            elif c=='*':
                stack.append(o1*o2)
            elif c=='/':
                stack.append(o1/o2)
    return stack.pop()
if __name__ == "__main__":
    exp="26*9+"
    print(evaluateexp(exp))
    

            


