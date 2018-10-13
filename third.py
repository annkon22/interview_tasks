import random as rnd
def listrand(lst, n = 10, rndran = 100):
    for _ in range(0, n):
        lst.append(rnd.randrange(0, rndran))
    return
my_lst = []
listrand(my_lst)
my_lst.sort()
my_lst.reverse()
print(my_lst)


step  = 0
for i in range(len(my_lst) -1):
    if step < 2:
        if my_lst[i] > my_lst[i + 1]:
            step += 1
            new = my_lst[i + 1]
        else: 
            continue
print('The third max:', new)

