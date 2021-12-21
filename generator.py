# -*- coding: utf-8 -*-
from scipy import stats

text = ['A','C','G','T']

data = (1,2,3,4)
pA = (9/18,3/18,5/18,1/18)
pC = (4/10,1/10,1/10,4/10)
pG = (2/8,1/8,0/8,5/8)
pT = (3/13,5/13,2/13,3/13)

A = stats.rv_discrete(values=(data,pA))
C = stats.rv_discrete(values=(data,pC))
G = stats.rv_discrete(values=(data,pG))
T = stats.rv_discrete(values=(data,pT))

def gen(start):
    res = []
    last = start
    for i in range(3):
        if last==1: last=A.rvs()
        elif last==2: last=C.rvs()
        elif last==3: last=G.rvs()
        else: last=T.rvs()
        res.append(last)
    return res

#A=1, C=2, G=3, T=4
#set value of last letter

last_letter = 1

print('{}{}{}'.format(*[text[i-1] for i in gen(last_letter)]))

