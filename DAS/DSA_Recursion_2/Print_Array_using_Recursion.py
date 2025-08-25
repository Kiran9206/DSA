
def print_array(A:list, idx=0):

    # step1: define a base condition
    if idx >= len(A):
        print()
        return
    #step2: print the array value
    print(A[idx], end=" ")

    # step3: call the same function by incrementing idx value by 1
    print_array(A,idx+1)
    print()


if __name__ == "__main__":
    A = [6, -2, 5, 3]
    print_array(A)