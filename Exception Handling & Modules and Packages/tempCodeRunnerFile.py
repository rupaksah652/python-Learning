try:
  with open('sample3.txt','r') as f:
    print(f.read())  
except:
   print('sorry file not found')     
