#accessing item

#for 1D
#indexing
print("for 1D")
t=(1,2,3,4,5)
print(t)
print(t[0])
print(t[-1])
print(t[0::])  #used for print all the element

#slicing
print("for slicing")
print(t[0:4:2])
print(t[-3:-1])
print(t[::-1])  #used for reverse

#for 2D
print("for 2D")
a=(1,2,3,(4,5,6))
print(a[3][0])
print(a[-1][1])
print(a[-1][2])
print(a[3][-1])