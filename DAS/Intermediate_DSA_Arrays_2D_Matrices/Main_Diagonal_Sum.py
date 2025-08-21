


def main_diagonal_sum(matrix: list)->int:
    sum = 0
    for idx in range(len(matrix)):
        sum+= matrix[idx][idx]

    return sum

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print("Main Diagonal Sum:", main_diagonal_sum(matrix))  # Output: 15

    matrix2 = [[1, 2],
               [3, 4]]
    print("Main Diagonal Sum:", main_diagonal_sum(matrix2))  # Output: 5
