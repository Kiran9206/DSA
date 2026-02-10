'''
Problem Description
Given an array of integers A, find and return the peak element in it.
An array element is considered a peak if it is not smaller than its neighbors. For corner elements, we need to
consider only one neighbor.

NOTE:
It is guaranteed that the array contains only a single peak element.
Users are expected to solve this in O(log(N)) time. The array may contain duplicate elements.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 109

Input Format
The only argument given is the integer array A.

Output Format
Return the peak element.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
Input 2:
A = [5, 17, 100, 11]

Example Output
Output 1:
 5
Output 2:
 100

Example Explanation
Explanation 1:
 5 is the peak.
Explanation 2:
 100 is the peak.
'''


# bruteforce approach...
def peak_ele(A: list)-> int:
    n = len(A)
    return max(A)


# optimised approach using binary search....

# I see the pattern over here it is increasing and decreasing manner

def peak_ele_opt(A: list)-> int:
    n = len(A)


    # edge cases
    if n == 1:
        return A[0]

    # strictly increasing..
    if A[n-1] > A[n-2]:
        return A[n-1]
    # strictly decreasing...
    if A[0]> A[1]:
        return A[0]

    start, end = 1, n-2
    # apply binary search...
    while(start <= end):
        mid = (start + end)//2

        # check if mid is peak element...
        if (A[mid-1] < A[mid] > A[mid+1]):
            return A[mid]

        elif (A[mid] > A[mid-1] and A[mid] < A[mid+1]):
            start = mid + 1

        else:
            end = mid - 1
    return -1


A = [5, 17, 100, 11]
A = [1, 2, 3, 4, 5]
print(peak_ele_opt(A))