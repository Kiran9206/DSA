


def parentheses(A: int, openCount: int, closeCount: int, strValue: list, ans: list) -> list:

    # step1 : set base condition...
    if len(strValue) == A * 2:
        ans.append(''.join(strValue))
        return ans
    if openCount < A:
        strValue.append('(')
        parentheses(A, openCount+1, closeCount, strValue, ans)
        strValue.pop() #backtracking step... since i'm using list to store the string value...

    if closeCount < openCount:
        strValue.append(')')
        parentheses(A, openCount, closeCount+1, strValue, ans)
        strValue.pop()#backtracking step... since i'm using list to store the string value...
    return ans



A = 3
print(parentheses(A,0,0,[],[]))