#dictionary function
#len/sorted/min/max
d={'name':'nitish','gender':'male','age':33}
print("len/sorted/min/max")
print(len(d))
print(sorted(d))
print(sorted(d,reverse=True))
print(min(d))
print(max(d))

#items/keys/values
print("items/keys/values")
print(d.items())
print(d.keys())
print(d.values())

#update
print("update")
d1={1:2,3:4,4:5}
d2={4:7,6:8}
d1.update(d2)
print(d1)
print(d2)