# bruteforce approach....

def check_anagram(A:str, B:str)-> int:
    if len(A) != len(B):
        return 0
    A = sorted(A)
    B = sorted(B)
    return 1 if A == B else 0



# frequency approach....

def check_anagram_frequency_approach(A:str, B:str)->int:

    if len(A) != len(B):
        return 0

    freq = [0] * 26 # Assuming only lowercase letters a-z,and it's a static length of 26

    for ch in A:  # Count frequency of each character in A
        freq[ord(ch) - ord('a')] += 1
    for ch in B: # Decrease frequency based on characters in B
        freq[ord(ch) - ord('a')] -= 1

    return 1 if all(ch == 0 for ch in freq) else 0

