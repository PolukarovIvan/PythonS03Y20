# map usages
lst1 = list(map(int, input().split()))
print(lst1)

# map unpacking
map_object = map(int, input().split())
a, b = map_object
print(a, b, sum((a, b)))

# map iteration
map_object = map(int, input().split())
a = next(map_object)
b = next(map_object)
print(a, b, sum((a, b)))
