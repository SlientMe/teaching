import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,10,100)  # 其实是折线图
print(x)
siny = np.sin(x)

cosy = np.cos(x)

plt.plot(x,siny,color="red",linestyle="--")
plt.plot(x,cosy)


plt.show()