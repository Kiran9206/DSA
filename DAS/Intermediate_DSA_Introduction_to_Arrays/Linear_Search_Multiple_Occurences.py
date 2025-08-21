def occurences(A:list, B:int)->int:
    count = 0
    for item in A:
        if item == B:
            count+=1
    return count

if __name__ == "__main__":
    A = [1, 2, 1]; B = 3
    print(occurences(A,B))