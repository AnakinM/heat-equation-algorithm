import math
import matplotlib.pyplot as plt
import pygame

def gen(min, max, step):
    x0 = int((min+max)/2)

    ran = int(((max - min) / step))
    steps = [min + step*i for i in range(1, ran+1)]

    inp = []
    for x in steps:
        inp.append(math.exp(-1 * ((x - x0) * (x - x0))))

    return inp

#print(gen(0, 10, .1))

# U_t = a * U _xx
def calc_this(ui, a, tau, h):
    denom = (1/(tau / 2)) + (2 / (h * h))
    l = 100
    res = [[i] for i in ui]
    #print(res)
    for j in range(1, len(ui) * 5):
        for i in range(len(res)):
            if i == 0:
                uj = ((res[i][j-1] / (tau / 2) ) + ((res[i+1][j-1]) / (h * h))) / denom

            if i == len(res) - 1:
                uj = ((res[i][j-1] / (tau / 2) ) + ((res[i-1][j-1]) / (h*h))) / denom

            else:
                uj = ((res[i][j-1] / (tau / 2) ) + ((res[i+1][j-1] + res[i-1][j-1]) / (h * h))) / denom

            res[i].append(uj)        
        

    uji = []
    for i in res:
        uji.append(i[-1])
    t = [tau * i for i in range(len(uji))]
    return uji, t

print(len(gen(0, 20, .05)))

x, t = calc_this(gen(0, 10, .05), 1., .05, .1)
x2, t2 = calc_this(gen(0, 10, .03), 1., .03, .1)
x3, t3 = calc_this(gen(0, 10, .01), 1., .01, .1)

plt.figure()
plt.plot(t, x)
plt.plot(t2, x2)
plt.plot(t3, x3)
plt.show()