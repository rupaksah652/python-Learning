#local and global variable 

a=2
def temp():
    #local var
    global a
    a+=1
    print(a)

temp()
print(a)