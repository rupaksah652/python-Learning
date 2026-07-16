#remove key value pair
d3={'name': 'rupak', 'age': 22, 'year': 3, 'gender': 'male', 'weight': 70}
#pop
#d3.pop('year')
#popitem
#d3.popitem()
#del
#del d3['name']
#clear
#d3.clear()
#print(d3)
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
#print(s['subject']['dsa'])
s['subject']['ds']=75
print(s)