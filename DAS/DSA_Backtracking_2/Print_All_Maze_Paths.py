


def maze_path(A:int, B:int, row=1, column=1,current_list: list = None, ans: list = None)->list:
    if current_list is None:
        current_list = []
    if ans is None:
        ans = []

    # basecase

    if row == A and column == B:
        ans.append(''.join(current_list))

    if row < A:
        current_list.append('D')
        maze_path(A,B,row+1, column, current_list, ans)
        current_list.pop() #backtracking....
    if column < B:
        current_list.append('R')
        maze_path(A,B,row,column+1, current_list, ans)
        current_list.pop() #backtracking....
    return ans

A = 3
B = 3
print(maze_path(A,B))