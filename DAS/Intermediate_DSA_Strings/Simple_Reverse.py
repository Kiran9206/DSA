def reverse_string(S:str)->str:

    return S[::-1] if S else ""


def revese_string_alt(S:str)-> str:
    reverse_string = []
    for i in range(len(S)-1,-1,-1):
        reverse_string.append(S[i])
    return ''.join(reverse_string)

# Input 1:
A = "scaler"
print(reverse_string(A))
print(revese_string_alt(A))
# Input 2:
A = "academy"
print(reverse_string(A))
print(revese_string_alt(A))