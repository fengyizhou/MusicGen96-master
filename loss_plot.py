import matplotlib.pyplot as plt
import numpy as np

g_loss = np.load("g_loss_list.npy")
d_loss = np.load("d_loss_list.npy")
gp = np.load("gp_list.npy")

g_loss = g_loss[:10000]
d_loss = d_loss[:10000]
gp = gp[:10000]
fig = plt.figure(figsize=(12,6))
colors = ['red', 'blue', 'green']


plt.plot(g_loss, c=colors[0])
plt.plot(d_loss, c=colors[1])
plt.plot(gp, c=colors[2])

plt.show()