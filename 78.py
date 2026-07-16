#operation on tuples
#1.arithmetic(+,*)
#2.membership
#3.iteration

#arithmetic
print("arithmetic")
t1=(1,2,3,4)
t2=(5,6,7,8)
print(t1+t2)
print(t1*2)

print("membership")
print(1 in t1)
print(5 in t1)
print(2 in t2)

#iteration 
print("iteration")
for i in t1:
    print(i)

