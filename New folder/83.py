#set operation 
s1={1,2,3,4,5}
s2={4,5,6,7,8}
#union(|)
print("union(|)")
print(s1|s2)

#intersection(&)
print("intersection(&)")
print(s1&s2)

#difference(-)
print("difference(-)")
print(s1-s2)
print(s2-s1)

#symmetric difference(^)
print("symmetric differnce(^)")
print(s1^s2)

#membership test
print("membership test")
print(1 in s1)
print(1 in s2)

#iteration 
print("iteration")
for i in s1:
    print(i)