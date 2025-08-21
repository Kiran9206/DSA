

def colsum(matrix: list)->list:

    collen = len(matrix[0])
    rowlen = len(matrix)
    ans = []

    for col in range(collen):
        sum = 0
        for row in range(rowlen):
            sum += matrix[row][col]
        ans.append(sum)
    return ans

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Column Sum:", colsum(matrix))  # Output: [12, 15, 18]

    matrix2 = [[1, 2], [3, 4], [5, 6]]
    print("Column Sum:", colsum(matrix2))  # Output: [9, 12]