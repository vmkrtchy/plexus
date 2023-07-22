def  kuku(ls1,ls2):
    flag = 0;
    for i in ls1:
        for j in ls2:
            if i == j:
                flag = 1
                return flag
print (kuku([1,2,3,4,5,6,7],[2,3,4,6,7,8,6,9,5]))
