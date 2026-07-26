#set function

#len/sum/min/max/sorted
s={2,31,1.3,1,3,11}
print("len/sum/min/max/sorted")
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s))
print(sorted(s,reverse=True))

#union/update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print("union/update")
print(s1.union(s2))
s1.update(s2)
print(s1)
print(s2)

#intersection/intersection_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print("intersection/intersection_update")
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
print(s2)

#difference/difference_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print("difference/difference_update")
print(s1.difference(s2))
s1.difference_update(s2)
print(s1)
print(s2)

#symmetric_difference/symmetric_difference_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print("symmetric_diffrence/symmetric_difference_update")
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)
print(s2)

#isdisjoint/issubset/issuperset
print("isdisjoint")
s1={1,2,3,4}
s2={3,4}
print(s1.isdisjoint(s2))

print("issubset")
print(s1.issubset(s2))

print("issuperset")
print(s1.issuperset(s2))

#copy
print("copy")
s1={1,2,3}
s2=s1.copy()
print(s1)
print(s2)