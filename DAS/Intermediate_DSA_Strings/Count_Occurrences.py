def occurence(S:str)-> int:
    count = 0
    for idx in range(len(S)):
        if S[idx:idx+3] == "bob":
            count+=1

    return count

def occurence_1(S:str)->int:
    return S.count('bob')