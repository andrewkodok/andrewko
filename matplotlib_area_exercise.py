import matplotlib.pyplot as plt
import random

random_x = []
random_y = []
total_y = []

for i in range(4000):
    random_x.append(random.randint(0, 25))
    random_y.append(random.randint(0, 600))

plt.plot(random_x, random_y, 'o', color = "black")

x = []
y = []

for i in range(0,26):
    x.append(i)
    y.append(i ** 2 - 3 * i + 4)

plt.plot(x , y, "o", color = "green")

for q in range(len(random_x)):
    num = x.index(random_x[q])

    if random_y[q] < y[num]:
        total_y.append(random_y[q])
    else:
        continue

print(len(total_y)/ 4000 * 25 * 600)

plt.title ("Calculating area under a graph", fontsize = 14)
plt.xlabel ("x coordinate", fontsize = 10)
plt.ylabel ("y coordinate", fontsize = 10)

plt.axis([0,25,0,600])
plt.show()
