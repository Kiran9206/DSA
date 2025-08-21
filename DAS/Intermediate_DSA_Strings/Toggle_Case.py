def toggle_case(string:str)->str:

    ans = []

    for char in string:
        if ord(char) >= 65 and ord(char) <= 90:
            ans.append(chr(ord(char)+32))
        elif ord(char) >= 97 or ord(char) <= 122:
            ans.append(chr(ord(char)-32))
        else:
            ans.append(char)
    return ''.join(ans)


def toggle_case_alternative(string:str)->str:
    return string.swapcase()


# Input 1:
A = "Hello"
print(toggle_case_alternative(A))
# Input 2:
A = "tHiSiSaStRiNg"
print(toggle_case_alternative(A))

