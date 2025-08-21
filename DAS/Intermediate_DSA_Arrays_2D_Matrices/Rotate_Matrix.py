def transpose(A:list)->list:
    rowlen = len(A)
    collen = len(A[0])
    for row in range(1,rowlen):
        for col in range(row):
            tem = A[row][col]
            A[row][col] = A[col][row]
            A[col][row] = tem
    return A

def rotate_90(A):
    A = transpose(A)
    print(A)
    rowlen = len(A)
    collen = len(A[0])

    for row in range(rowlen):
        i = 0; j = collen - 1
        while i<j:
            temp = A[row][i]
            A[row][i] = A[row][j]
            A[row][j] = temp
            i+=1; j-=1
    return A

if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
     ]
    print(rotate_90(A))
