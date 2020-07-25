import itertools 
S=input()
key_func = lambda x: x[0]
for key, group in itertools.groupby(S, key_func): 
    print('('+str(len(list((group))))+', '+key+')',end=' ')
