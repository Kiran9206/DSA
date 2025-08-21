def amazing_subarray(S:str)->int:
    count = 0
    n=len(S)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for idx, char in enumerate(S):
        if char in vowels:
            count += (n - idx)
    return count
