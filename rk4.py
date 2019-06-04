import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generates Gauss function
def generate_gauss(min, max, step):
    x0 = int((min+max)/2)

    ran = int(((max - min) / step))
    steps = [min + step*i for i in range(1, ran+1)]

    inp = []
    for x in steps:
        inp.append(math.exp(-1 * ((x - x0) * (x - x0))))

    return inp, step

#print(gen(0, 10, .1))

# U_t = a * U _xx
def thermal_conductivity(ui, a, tau, h):
    denom = (1/(tau / 2)) + (2 / (h * h))
    l = 100
    res = [[i] for i in ui]
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
        uji.append(a * i[-1])
    t = [tau * i for i in range(len(uji))]
    return uji, t

print(len(generate_gauss(0, 20, .05)))

x = []
for i in range(1, 100):
    x.append(generate_gauss(0, 10, .5 / i))
#plt.figure()
#x.reverse()
#y = []

#for g in x:
    #y.append(thermal_conductivity(g[0], 1., g[1], .01))

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
x.reverse()
def animate(i):
    y = thermal_conductivity(x[ i % len(x) ][0], 1., x[ i % len(x) ][1], .01)
    ax1.clear()
    ax1.plot( y[1], y[0] )

    plt.axis([0, 10, 0, 0.8])
    plt.xlabel("Ciepło")
    plt.ylabel("Czas")
    plt.title("Rozchodzenie się ciepła")

ani = animation.FuncAnimation(fig, animate, interval = 800)
plt.show()