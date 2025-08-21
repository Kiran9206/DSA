def Reverse_string(S:str)-> str:

    arr = S.split(" ")
    arr.reverse()
    return ' '.join(arr).strip()

# Input 1:
A = "the sky is blue"
print(Reverse_string(A))
# Input 2:
A = "this is ib"
print(Reverse_string(A))