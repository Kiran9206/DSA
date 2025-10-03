'''
Problem Description
You are given an array A of N integers. Return the count of elements with frequency 1 in the given array.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
First argument A is an array of integers.

Output Format
Return an integer.

Example Input
Input 1:
A = [3, 4, 3, 6, 6]
Input 2:
A = [3, 3, 3, 9, 0, 1, 0]

Example Output
Output 1:
1
Output 2:
2

Example Explanation
Explanation 1:
Only the element 4 has a frequency 1.
Explanation 2:
The elements 9 and 1 has a frequncy 1.
'''
from itertools import count


# brute force approach...

def frequency(A: list) -> int:
    count = 0
    for i in range(len(A)):
        freq = 0
        for j in range(len(A)):
            if A[i] == A[j]:
                freq += 1
                if freq > 1:
                    break
        if freq == 1:
            count += 1
    return count



# optimised approach using frequency / hashmap

def frequency_opt(A: list)-> int:
    # Step1: set the frequency for all the elements in the list
    hash_map = {}
    for item in A:
        if item in hash_map:
            hash_map[item] += 1
        else:
            hash_map[item] = 1
    # step2: check the frequency of each element and count the elements which are 1
    freq = 0
    for item in hash_map:
        if hash_map[item] == 1:
            freq+=1
    return freq





import pytest

def test_frequency():
    A = [3, 3, 3, 9, 0, 1, 0]
    assert frequency(A) == 2 #positive
    assert isinstance(A, list)

def test_frequency_opt():
    A = [3, 3, 3, 9, 0, 1, 0]
    assert frequency_opt(A) == 2





