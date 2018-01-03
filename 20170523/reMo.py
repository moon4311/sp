import re, glob

p = re.compile('.*M*.p*')
for i in glob.glob('*'):
    m = p.match(i)
    if m :
        print(m.group())
