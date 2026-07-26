#deleting a item from a list

#use of del keyword
a=[1,2,3,4,5,6]
del a

#indexing 
b=[1,2,3,4,5,6]
del b[-1]
print(b)

#slicing
del b[1:3]
print(b)

#use of remove keyword
c=[1,2,3,4,5,6]
c.remove(2)
print(c)

#use of pop keyword
d=[1,2,3,4,5,6]
d.pop()
print(d)

#use of clear keyword
e=[1,2,3,4,5,6]
e.clear()
print(e)

