from time import process_time

start = process_time()

n = 2 ** 10
L = list(range(2, n))
L2 = L[:] # https://stackoverflow.com/a/10665602

for p in L:
    for q in L:
        if (q in L2) and (q != p and q % p == 0):
            L2.remove(q)

end = process_time()

print('elapsed:', end - start)
#print(L2)
