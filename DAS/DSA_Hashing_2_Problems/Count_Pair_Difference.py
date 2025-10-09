'''
Problem Description
You are given an array A of N integers and an integer B.
Count the number of pairs (i,j) such that A[i] - A[j] = B and i ≠ j.
Since the answer can be very large, return the remainder after dividing the count with 109+7.
Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109
1 <= B <= 109

Input Format
First argument A is an array of integers and second argument B is an integer.

Output Format
Return an integer.

Example Input
Input 1:

A = [3, 5, 1, 2]
B = 4
Input 2:
A = [1, 2, 1, 2]
B = 1

Example Output
Output 1:
1
Output 2:
4
Example Explanation
Example 1:
The only pair is (2, 3) which gives difference as 4
Example 2:
The pair which gives difference as 3 are (2, 1), (4, 1), (2, 3) and (4, 3). 
'''

# brute force

def countPairDiff(A:list, B:int)-> int:
    count = 0
    MOD = 10 ** 9 + 7
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j and (A[i] - A[j]) == B:
                count+=1
    return count % MOD

# optimisation using hashset
def countPairDiff1(A:list, B:int)-> int:
    count = 0
    freq = {}
    MOD = 10 ** 9 + 7
    #steup the frequency of all the elements in A
    for item in A:
        freq[item] = freq.get(item,0) + 1
    # check the valid pair diff
    for item in A:
        target = item - B
        if target in freq:
            count=(count + freq[target])%MOD
    return count

if __name__ == "__main__":
    A = [3, 5, 1, 2]
    B = 4
    A = [1, 2, 1, 2]
    B = 1
    print(countPairDiff(A,B))
    print(countPairDiff1(A,B))
