# bruteforce approach...

def palindrom(s: str, start: int, end: int) -> bool:
    while start < end:
        if s[start] != s[end]:
            return False
        start+=1; end-=1
    return True

def longest_palindrome(s: str) -> str:
    ans = 0; result = ""
    for start in range(len(s)):
        for end in range(start, len(s)):
            if palindrom(s,start,end):
                longest_palindrome = end - start + 1
                if ans < longest_palindrome:
                    ans = longest_palindrome
                    result = s[start:end+1]
    return result




# optimized approach using expand around center technique


def expand(s: str, left: int, right: int) -> list:
    while left >=0 and right < len(s):
        if s[left] == s[right]:
            left -= 1
            right += 1
        else:break
    return [left+1, right-1, right - left -1]  # return start, end, length


def longest_palindrome_opt(s:str) -> str:
    ans = 0; result  = ''
    for idx in range(len(s)):
        # odd palindrome
        l, r = idx, idx
        start, end, length = expand(s, l, r)
        if length > ans:
            ans = length
            result = s[start:end+1]
        # even
        start, end, length = expand(s, l, r+1)
        if length > ans:
            ans = length
            result = s[start:end + 1]
    return result



# Example usage
if __name__ == "__main__":
    input_string = "babad"
    result = longest_palindrome_opt(input_string)
    print(f"The longest palindromic substring in '{input_string}' is: '{result}'")
    # Input
    # 1:
    A = "aaaabaaa"
    print(longest_palindrome_opt(A))
    # Input
    # 2:
    A = "abba"
    print(longest_palindrome_opt(A))


