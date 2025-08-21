# brute force approach

def find_perfect_numbers(n):

    sum_of_factor = 0
    for idx in range(1,n):
        if n % idx == 0:
            sum_of_factor += idx

    if sum_of_factor == n:
        return 1
    else: return 0


# optimized approach
def find_perfect_numbers_optimized(n):

    sum_of_factor = 0
    for idx in range(1, int(n**0.5)+1):
        if n % idx == 0:
            if n/idx == idx:
                sum_of_factor += idx
            sum_of_factor+= n // idx



