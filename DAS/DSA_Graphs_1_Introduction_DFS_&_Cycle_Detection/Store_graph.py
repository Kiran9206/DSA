# -> adjecency matrix representation of graph

from typing import List

def adj_matrix_rep(edges: List[List[int]])-> List[List[int]]:

    n = max(max(u,v) for u,v in edges)+1
    matrix = [[0 for _ in range(n)] for _ in range(n)]


    for edge in edges:
        node = edge[0]
        neighbor = edge[1]
        matrix[node][neighbor] = 1
    return matrix



# -> adjecency list representation of graph

def adj_list_rep(edges: List[List[int]])-> List[List[int]]:

    n = max(max(u,v) for u,v in edges) + 1
    adj_list = [[] for _ in range(n)]


    for edge in edges:
        node = edge[0]
        neighbor = edge[1]
        adj_list[node].append(neighbor)

    return adj_list



