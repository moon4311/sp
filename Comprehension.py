import os

print(os.getcwd())

os.chdir('C:\\/Users/')
print(os.getcwd() , " : os.chdir('PATH') - > 경로이동" )


print(os.path.join('/Users/pilgrim/diveintopython3/examples/', 'humansize.py'))

print(os.path.join('/Users/pilgrim/diveintopython3/examples', 'humansize.py'))

print(os.path.expanduser('~'))

print(os.path.join(os.path.expanduser('~'), 'diveintopython3', 'examples', 'humansize.py'))


pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
os.path.split(pathname)
(dirname, filename) = os.path.split(pathname)
print('split() # , 기준 -> dirname : ' , dirname , ' / filename : ', filename)
(shortname, extension) = os.path.splitext(filename)
print('splitext() # . 기준 - > shortname : ' , shortname , '/ extension : ' , extension)


# 3.2.3 Listing Directories
# os.chdir('/Users/pilgrim/diveintopython3/')
import glob
