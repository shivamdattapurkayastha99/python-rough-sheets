def balanceparen(exp):
    stack=[]
    for char in exp:
        if char in ["(","{","["]:
            stack.append(char)
        else:
            if not stack:
                return False
            currentchar=stack.pop()
            if currentchar=="(":
                if char!=")":
                    return False
            if currentchar=="[":
                if char!="]":
                    return False
            if currentchar=="{":
                if char!="}":
                    return False
    if stack:
        return False
    return True
if __name__ == "__main__":
    exp=input("Enter the expression to check balanced parenthesis")
    if balanceparen(exp):
        print("balanced\n")
    else:
        print("not balanced\n")