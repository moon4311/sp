import os

print(os.getcwd())

print(os.listdir(os.getcwd()))

os.rename(os.listdir(os.getcwd())[6],'newss.txt')

print(os.listdir(os.getcwd()))


