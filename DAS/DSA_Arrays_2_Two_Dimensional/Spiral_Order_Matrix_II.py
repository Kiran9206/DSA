# bruteforce approach....
from typing import List



def generateMatrix(A: int)->List[List[int]]:
    if A == 0:
        return []
    if A == 1:
        return [[1]]
    n = A
    # initialize the matrix with value 0
    ans = [[0 for _ in range(n)] for _ in range(n)]

    i = j = 0
    num = 1
    while n > 1:
        for _ in range(n-1):
            ans[i][j] = num
            num+=1; j+=1
        for _ in range(n-1):
            ans[i][j] = num
            num+=1; i+=1
        for _ in range(n-1):
            ans[i][j] = num
            num+=1; j-=1
        for _ in range(n-1):
            ans[i][j] = num
            num+=1; i-=1

        # move to the inner matrix
        i += 1; j += 1
        n-=2 #elemening the outer layer
        if n == 1:
            ans[i][j] = num
            break
    return ans


if __name__ == "__main__":
    n = 1
    print(generateMatrix(n))
    n = 3
    print(generateMatrix(n))
    n = 4
    print(generateMatrix(n))
    n = 5
    print(generateMatrix(n))
    n = 6
    print(generateMatrix(n))
    n = 7
    print(generateMatrix(n))
    n = 8
    print(generateMatrix(n))