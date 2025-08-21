


# brute force approach

def count_factors(n):
    count  = 0
    for idx in range(1, n+1):
        if n % idx == 0:
            count+=1
        else: continue
    return count

# optimized approach

def count_factors_optimized(n):
    count = 0
    # n = x * y => y = n / x

    for idx in range(1, int(n**0.5)+1):
        if n % idx == 0:
            if idx * idx == n:
                count += 1
            else:
                count += 2
    return count

# Test the functions
if __name__ == "__main__":
    n = 24
    print("Brute Force Count of Factors:", count_factors(n))  # Output: 6
    print("Optimized Count of Factors:", count_factors_optimized(n))  # Output: 6

    n = 10
    print("Brute Force Count of Factors:", count_factors(n))  # Output: 6
    print("Optimized Count of Factors:", count_factors_optimized(n))  # Output: 6