import numpy as np
import matplotlib.pyplot as plt

tri = np.array([[1,1],[3,1],[2,3]])

centroid = tri.mean(axis = 0)
print(centroid)


trishape = plt.Polygon(tri, edgecolor='r', alpha=0.2, lw=5)
_, ax = plt.subplots(figsize=(4, 4))
ax.add_patch(trishape)
ax.set_ylim([.5, 3.5])
ax.set_xlim([.5, 3.5])
ax.scatter(*centroid, color='g', marker='D', s=70)
ax.scatter(*tri.T, color='b',  s=70)

plt.show()