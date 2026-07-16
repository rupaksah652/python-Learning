#let's create a file
with open('sample.txt','w') as f:
    f.write('hello world')


#try catch demo
try:
  with open('sample3.txt','r') as f:
    print(f.read())  
except:
   print('sorry file not found')     
