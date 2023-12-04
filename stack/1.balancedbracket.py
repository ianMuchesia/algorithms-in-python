def isMatch(p1,p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False
    
def balanced_bracket(brackets):
    opening = "({["
    stack = []
    
    if not len(brackets):
        return False
    
    i = 0
    
    if brackets[0] not in opening:
        return False
    
    while i < len(brackets):
     
        if brackets[i] in opening:
            stack.append(brackets[i])
           
        else:
            if(not len(stack)):
                return False
            
            if isMatch(stack[-1], brackets[i]):
                
                stack.pop()
            else:
                return False
        i+=1
        print("stack",stack)
    
    return len(stack) == 0


print(balanced_bracket("(((({}))))"))
    
def balanced_bracket(brackets):
    opening = "({["
    stack = []

    for bracket in brackets:
        if bracket in opening:
            stack.append(bracket)
        else:
            if not stack or not isMatch(stack.pop(), bracket):
                return False
        print("stack", stack)

    return not stack
