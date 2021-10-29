def purefunction(oldlist):
    list1 =[]
    for i in oldlist:
        list1.append(i**2)
    return list1


oldlist = [1,2,3,4]
modified_list = purefunction(oldlist)
print(modified_list)

