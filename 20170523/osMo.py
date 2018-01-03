import os

dirs=os.listdir()
f = open(dirs[2])
tt=f.read()
print(tt)

'''
letter = open(os.getcwd()+'\letter1.txt','w')
letter.write('Dear Father,')
letter.close()
'''

# os.remove(os.getcwd()+'\letter2.txt')