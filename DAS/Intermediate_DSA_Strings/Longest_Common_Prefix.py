def longest_common_prefix(S:list)-> str:
    ans = []
    if not S:
        return ""

    prefix = S[0]
    for word in range(1,len(S)):
        while S[word][:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


# Input 1:
A = ["abcdefgh", "aefghijk", "abcefgh"]
print(longest_common_prefix(A))
# Input 2:
A = ["abab", "ab", "abcd"];
print(longest_common_prefix(A))




