#accesing items from a list

#indexing

#positive(for 1D)
L=[1,2,3,4,5]
print(L[0])

#negative
print(L[-1])

#positive(for 2D)
a=[1,2,3,[4,5]]
print(a[3][0])
#negative(for 2D)
print(a[-1][-1])


#positive(for 3D)
b=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(b[1][0][0])
print(b[0][0][1])

#negative(for 3D)
print(b[-1][-1][-1])