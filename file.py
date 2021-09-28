f = open("text.txt") 
f = open("text.txt",'w')
f = open("text.txt",'r+b')
f.close()

with open("text.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")