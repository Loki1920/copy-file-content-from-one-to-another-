# copy file content from one to another file 

f1 = open('s.txt','r')# file from data will be copied
f2 = open('s1.txt','w')#file in which copied data is written

d = f1.read()
print(d)
f2.write(d)
f1.close()
f2.close()
