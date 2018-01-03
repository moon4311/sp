def getTotalPage(total,pagePer):
    data = total // pagePer
    if total % pagePer > 0:
        data += 1
    return data

res=getTotalPage(30,10)
print(res)

