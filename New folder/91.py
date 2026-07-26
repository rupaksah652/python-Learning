#dictionary operation

#membership
s={
    'name':'rupak',
    'college':'kiit',
    'sem':4,
    'subject':{
        'dsa':80,
        'math':60,
        'english':80
    }
}
print('nitish'in s)
print('name' in s)

#iteration
for i in s:
    print(i,s[i])