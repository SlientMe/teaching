# 梯度下降法
# 不是一个机器学习算法
# 是一个基于搜索的最优化方法
import numpy as np
import matplotlib.pyplot as plt

plot_x = np.linspace(-1,6,141)
plot_y = (plot_x-2.5)**2-1
plt.plot(plot_x,plot_y)
plt.show()

# x坐标就是theta
def dj(theta): # 导函数
    return 2*(theta-2.5)

def j(theta):  # 损失函数
    return (theta-2.5)**2 -1

theta = 0.0  # 初始点
epsilon = 1e-8 # 精确度
eta = 0.1
while True:
    gradit = dj(theta) # 当前的梯度
    last_theta = theta
    theta = theta-eta*gradit

    if (abs(j(theta)-j(last_theta))<epsilon):
        break
print(theta)
print(j(theta))

# 图示画出来
theta = 0.0  # 初始点
theta_history = [theta]
while True:
    gradit = dj(theta) # 当前的梯度
    last_theta = theta
    theta = theta-eta*gradit
    theta_history.append(theta)

    if (abs(j(theta)-j(last_theta))<epsilon):
        break
plt.plot(plot_x,j(plot_x))
plt.plot(np.array(theta_history),j(np.array(theta_history)),color="red",marker="*")
plt.show()