#opertions on list

#arithmetic
a1=[1,2,3,4,5]
a2=[1,6,7,8,9]

#concatenation/merge
print(a1+a2)
#multipication
print(a1*2)


#membership
b1=[1,2,3,4,5,6]
b2=[7,8,9,10,[5,6]]
print(5 in b1)
print(6 not in b1)
print(5 in b2)
print([5,6] in b2)

#loops
b1=[1,2,3,4,5,6]
b2=[7,8,9,10,[5,6]]
for i in b1:
    print(i)
for j in b2:
    print(j)    