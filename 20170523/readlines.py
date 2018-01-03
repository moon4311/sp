import os
f = open(os.getcwd()+"\Python_for_fun.txt")
'''
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
'''

for x in range(5):
    line = f.readline()
    print(line)

lines = f.readlines()
import sys
sys.stdout.writelines(lines[:5])
