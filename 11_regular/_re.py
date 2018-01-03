import re


p = re.compile('[a-z]+')


# match <- 일치여부
m = p.match("python")
print(m)

# search  <- 포함여부

m = p.search("python")
print(m)

