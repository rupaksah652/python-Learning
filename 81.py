#creating sets

#empty
print("empty")
s=set()
print(s)
print(type(s))

#1D
print("1D")
s={1,2,3}
print(s)
print(type(s))

#homo and hetro
print("homo and hetro")
s1={1,'hello',4.5,True}
s2={1,'hello',4.5,(1,2,3)}
print(s1)
print(s2)

#using type conversion
print("type conversion")
s4=set([1,2,3])
print(s4)

#duplicate not allowed
print("duplicate not allowed")
s5={1,1,2,2,3,3,5,5,44,44}
print(s5)

#sets canot have mutable items
print("sets canot have mutable items")

#sets are unorderd
print("sets are unorderd")
a1={1,2,3}
a2={2,3,1}
print(a1==a2)