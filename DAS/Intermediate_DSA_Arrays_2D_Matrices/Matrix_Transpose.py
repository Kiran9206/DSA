
def transpose(matrix:list)->list:
    transpose = []; rowlen = len(matrix); collen = len(matrix[0])
    for col in range(collen):
        temp = []
        for row in range(rowlen):
            temp.append(matrix[row][col])
        transpose.append(temp)
    return transpose

if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transpose(A))