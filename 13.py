array =[]
for i in range(3):
    a = []
    for j in range(4):
        b = []
        for _ in range(6):
            b.append('*')
        a.append(b)
    array.append(a)
print(array)

array = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]

