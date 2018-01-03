import os
'''
users = {'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
f = open(os.getcwd()+'/users.txt', 'bw+')
import pickle
pickle.dump(users, f)
f.close()
'''
import pickle
f = open(os.getcwd()+"/users.txt")
a = pickle.load(f)
print (a)

