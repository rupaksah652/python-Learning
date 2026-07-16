#list comprehension

#add 1 to 10 number in a list
a=[i for i in range(1,11)]
print(a)

#scalar multiplication ona vector 
v=[2,3,4]
s=-3
print([s*i for i in v])

#add square 
a=[2,4,5]
print([i**2 for i in a])

#print all the number divisible by 5 in the range of 50
print([i for i in range(1,51) if i%5==0])

#find the language which start with letter p
languages=['java','python','php','c','javascript']
print([i for i in languages if i.startswith('p')])

#nested if with list comprehension 
basket=['apple','guava','cherry','banana']
my_fruits=['apple','kiwi','graps','banana']
#add new list from my_fruits and items if the fruits exists in basket and also starts with 'a'
print([i for i in my_fruits if i in basket if i.startswith('a')])

# print a (3,3) matrix using list comprehension -> nested list comprehension
print([i*j for i in range(1,4) for j in range(1,4)])

# cartesian product -> list comprehension on 2 list together
a1=[1,2,3,4]
a2=[5,6,7,8]
print([i*j for i in a1 for j in a2])