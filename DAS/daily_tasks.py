# Squares of odd numbers from 1–30
# Return only squares of odd numbers.
from operator import index

print([x**2 for x in range(1,30) if x % 2 != 0])
data = [[1,2,3],[4,5,6],[7,8,9]]
print([num for row in data for num in row if num % 3 == 0])

keys = ['a','b','c']
values = [10,20,30]

print({keys[i]:values[i] for i in range(len(keys))})
print(dict(zip(keys, values)))
nums = [4,7,10,15,18]

print([num for num in nums if num % 2 == 0])
print([num for num in nums if num % 2 != 0 and num < 0])


# Return numbers between 1–50 divisible by both 4 and 6.

print([num for num in range(1,51) if num % 4 == 0 and num % 6 == 0])
print([num for num in range(1,51) if num % 12 == 0])


# 🟡 Part 2 — Lambda Practice (5 Problems)
# 1️⃣ Square using lambda
square = lambda x: x**2
print(square(5))


# 2️⃣ Sort list of tuples by second value
data = [(1,5),(2,3),(4,1)]
sorted_data = sorted(data, key=lambda x:x[1])
print(sorted_data)
# 3️⃣ Filter even numbers using lambda

nums = [1,2,3,4,5,6]
filtered_data = list(filter(lambda x: x % 2 == 0, nums))
print(filtered_data)
# 4️⃣ Use lambda with map() to uppercase names

names = ["kiran", "raj", "anita"]
mapped_data = list(map(lambda x: x.upper(), names))
print(mapped_data)


# 5️⃣ Sort dictionary by values using lambda

data = {'a': 3, 'b': 1, 'c': 2}
dict_data = dict(sorted(data.items(), key=lambda x: x[1]))
print(dict_data)



l = ['a','b',1, 2,3,4]
# print(type(bool,l))
print(l.index('a'))

nums = [10,15,20,25,30]
print([num * 2 for num in nums if num % 5 == 0])
print(["even" if num % 2 == 0 else "odd" for num in nums])
matrix = [[1,2],[3,4],[5,6]]
print([num for row in matrix for num in row])
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
print({keys[i]: values[i] for i in range(len(keys))})
data = {'a':5, 'b':2, 'c':8}
print({K: V for K, V in data.items() if V > 5})
