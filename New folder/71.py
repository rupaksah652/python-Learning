# list function

#len/min/max/sorted
print("for len/min/max/sorted")
a=[10,3,45,5,3]
print(len(a))
print(min(a))
print(max(a))
print(sorted(a))
print(sorted(a,reverse=True))

#count
print("for count")
b=[1,3,523,53,43]
print(b.count(5))
print(b.count(1))
print(b.count(3))

#index
print("for index")
c=[1,3,523,53,43]
print(c.index(53))

#reverse
print("reverse")
d=[1,3,523,53,43]
d.reverse()
print(d)

#sort(vs sorted)
print('sort vs sorted')
e=[1,3,523,53,43]
print(e)
print(sorted(e))
print(e)
e.sort()
print(e)

#copy
print("for copy")
f=[1,2,3,4,5]
print(f)
print(id(f))
f1=f.copy()
print(f1)
print(id(f1))

