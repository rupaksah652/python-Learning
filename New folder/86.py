#dictionary
#crate dictionary

#empty dictionary
d={}
print(d)
print(type(d))

#1D dictionary
print("1D dictionary")
d1={'nitish':
'male'}
print(d1)
print(type(d1))

#with mixed key
print("with mixed key")
d2={(1,2,3):1,'nitish':'world'}
print(d2)

#2D dictionary/JSON
print("2D dictionary/JSON")
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
print(s)

#using sequence and dict function
print("using sequence and dict function")
d3=dict([('name','rupak'),('age',22),('year',3)])
print(d3)

#duplicate key
print("duplicate key")
d4={'name':'nitish','name':'rupak'}
print(d4)

#mutable items as key
print("mutable items as key")
d5={'name':'nitish',(1,2,3):2}
print(d5)