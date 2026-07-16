#local and global -> global created inside local 
def temp():
    #local var
    global a
    a=1
    print(a)
temp()
print(a)
