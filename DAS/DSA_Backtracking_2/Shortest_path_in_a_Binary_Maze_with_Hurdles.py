
from typing import List
def shortest_path(maze: List[List[int]], sr: int, sc: int, dr: int, dc: int, check: List[List[bool]], current_ans=0, final_ans=None):

    if final_ans is None:
        final_ans = [float('inf')]
    # step1: base case / edge case
    if sc < 0 or sc >= len(maze[0]) or sr < 0 or sr >= len(maze) or check[sr][sc] or maze[sr][sc]==0:
        return final_ans[0]

    # base case
    if sr == dr and sc == dc:
        final_ans[0] = min(final_ans[0], current_ans)
        return final_ans[0]

    # initialize all the paths
    left = sc - 1
    right = sc + 1
    top = sr - 1
    down = sr + 1

    # step2: move to all the ways(left, right, top, down)

    # before that make the element in check matrix as true since it's visited....
    check[sr][sc] = True
    shortest_path(maze, sr, left, dr, dc, check,current_ans+1,final_ans)  #move towards left....
    shortest_path(maze, sr, right, dr, dc, check,current_ans+1,final_ans)  #move towards right....
    shortest_path(maze, top, sc, dr, dc, check,current_ans+1,final_ans)  #move towards top....
    shortest_path(maze, down, sc, dr, dc, check,current_ans+1,final_ans)  #move towards top....

    #step3: backtrack by make the visited element as unvisited.....
    check[sr][sc] = False
    return final_ans[0]


if __name__ == "__main__":
    A = [[1, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]

    B, C = 0, 0  # Starting point (0,0)
    D, E = 3, 3  # Destination (3,3)
    check = [[False] * len(A[0]) for _ in range(len(A))]  # Visited cells initialization
    print(shortest_path(A,B,C,D,E,check))

