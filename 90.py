#editing key value pair
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
s['sem']=5
s['subject']['dsa']=90
print(s) 