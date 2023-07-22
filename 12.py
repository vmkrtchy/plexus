def removing045(lst):
    if len(lst) >= 5:
        res = [x for (i,x) in enumerate(lst) if i not in (0,4,5)]
    return res
def removing045_2(lst):
    res = [lst[i] for i in range(len(lst)) if i not in [0,4,5]]
    return(res)
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
res = []
res = removing045_2(color)
print (color,res)

