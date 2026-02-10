'''
Problem Description
Misha likes finding all Subarrays of an Array. Now she gives you an array A of N elements and told you to find the number
of subarrays of A, that have unique elements.
Since the number of subarrays could be large, return value % 109 +7.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 106

Input Format
The only argument given is an Array A, having N integers.

Output Format
Return the number of subarrays of A, that have unique elements.

Example Input
Input 1:
 A = [1, 1, 3]
Input 2:
 A = [2, 1, 2]

Example Output
Output 1:
 4
Output 1:
 5

Example Explanation
Explanation 1:
 Subarrays of A that have unique elements only:
 [1], [1], [1, 3], [3]
Explanation 2:
 Subarrays of A that have unique elements only:
 [2], [1], [2, 1], [1, 2], [2]
'''


# brute force
def countSubarrays(A):
    mod = 10**9 + 7
    sub_array_list = []
    for start in range(len(A)):
        for end in range(start,len(A)):
            subarray = A[start:end+1]
            if len(subarray) == len(set(subarray)):
                sub_array_list.append(subarray)
    return len(sub_array_list) % mod

# carry forward
def count_sub_arrays(A):
    mod = 10**9 + 7
    count = 0
    for start in range(len(A)):
        seen = set()
        for end in range(start,len(A)):
            if A[end] in seen:
                break
            seen.add(A[end])
            count+=1
    return count % mod



if __name__ == "__main__":
    A = [1, 1, 3]
    print(countSubarrays(A))
    print(count_sub_arrays(A))