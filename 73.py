#2 ways to traverse a list

#itemwise 
print("for item wise")
a=[1,2,3,4]
for i in a:
    print(i)



#indexwise
print("for indexwise")
a=[1,23,4,5]
print("for index address")
for i in range(0,len(a)):
     print(i)

print("for value")
for i in range(0,len(a)):     
     print(a[i])