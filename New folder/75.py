#lists are mutable
print("for mutable")
a=[1,2,3]
b=a
print(a)
print(b)
a.append(4)
print(a)
print(b)

print("for non mutable")
a=[1,2,3]
b=a.copy()
print(a)
print(b)
a.append(4)
print(a)
print(b)

