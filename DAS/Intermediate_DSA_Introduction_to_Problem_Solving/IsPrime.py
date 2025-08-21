

# brute force approach

def factors(n):
    count = 0
    for idx in range(1, n + 1):
        if n % idx == 0:
            count += 1
    return count

def is_prime(n):
    # edge case ...
    if n <= 1:
        return False

    factor = factors(n)
    if factor <= 2:
        return True
    else: return False

# optimized approach

def is_prime_optimized(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    for idx in range(2, int(n**0.5)+1):
        if n % idx == 0:
            return False
    return True

# Test the functions
if __name__ == "__main__":
    n = 29
    print("Brute Force Is Prime:", is_prime(n))  # Output: True
    print("Optimized Is Prime:", is_prime_optimized(n))  # Output: True

    n = 10
    print("Brute Force Is Prime:", is_prime(n))  # Output: False
    print("Optimized Is Prime:", is_prime_optimized(n))  # Output: False
