lst = list(range(1,50))
res = [i for i in lst if i % 2 != 0]
res2 = list(filter(lambda i:i%2 != 0,lst))
print (res2)

