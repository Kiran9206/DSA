def row_sum(A:list)->list:
    row = len(A)
    column = len(A[0])
    arr = []
    for r in range(row):
        row_sum = 0
        for c in range(column):
            row_sum += A[r][c]
        arr.append(row_sum)
    return arr