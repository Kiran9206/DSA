from ansible.module_utils.common.collections import count


def time_to_equality(A):
    sec = 0
    max_val = max(A)
    for item in A:
        sec+= (max_val - item)
    return sec

if __name__ == "__main__":
    A = [1, 2, 3, 4]
    print(time_to_equality(A))  # Output: 6
    A = [2, 5, 6]
    print(time_to_equality(A))  # Output: 5
    A = [1, 1, 1]
    print(time_to_equality(A))  # Output: 0