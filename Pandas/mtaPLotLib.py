import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd


"""Basic Graph"""

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, label='2x', color='red', linewidth=1, marker='*')

plt.title('Our 1st graph')
plt.xlabel('X')
plt.ylabel('Y')

plt.xticks([0, 1, 2, 3, 4])
plt.yticks([0, 2, 4, 6, 8, 10])

plt.legend()

plt.show()

