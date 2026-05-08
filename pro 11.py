
n = int(input())


numbers = list(map(int, input().split()))


transformed = [x**2 if x % 2 == 0 else x**3 for x in numbers]

print(tuple(transformed))
