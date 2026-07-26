#zip

#write a program to add items of 2 lists indexwise
a1=[1,2,3,4]
a2=[-1,-2,-3,-4]
print(list(zip(a1,a2)))
print([i+j for i,j in zip(a1,a2)])
