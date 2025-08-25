# approach1

def fast_power(base, exponent):
    if exponent == 0:
        return 1
    return base * fast_power(base, exponent - 1)

base = 2
exponent = 4
result = fast_power(base, exponent)
print(f"{base}^{exponent} = {result}")

# approach2
def fast_power_optimized(base, exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        return fast_power_optimized(base, exponent // 2) * fast_power_optimized(base, exponent // 2)
    else:
        return fast_power_optimized(base, exponent // 2) * fast_power_optimized(base, exponent // 2) * base

print(fast_power_optimized(base, exponent))

# approach3
def fast_power_optimized_1(base, exponent):
    if exponent == 0:
        return 1
    half_power = fast_power_optimized_1(base, exponent//2)
    if exponent % 2 == 0:
        return half_power * half_power
    else:
        return half_power * half_power * base