import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,10,100)  # 其实是折线图
print(x)
siny = np.sin(x)

cosy = np.cos(x)
plt.title("Test")
plt.plot(x,siny,color="red",linestyle="--",label="sin(x)")
plt.plot(x,cosy,label="cos(y)")
plt.xlabel("x values") # x轴的名字
plt.ylabel("y values")
# plt.xlim(-5,15) # x轴的坐标长度
# plt.ylim(0,1.5) # y轴的坐标长度
plt.legend()
plt.show()

# 散点图
plt.scatter(x,siny)
plt.scatter(x,cosy,color="red")
plt.show()

tx = np.random.normal(0,1,10000)
ty = np.random.normal(0,1,10000)
plt.scatter(tx,ty,alpha=0.2)  # alpha 透明度
plt.show()