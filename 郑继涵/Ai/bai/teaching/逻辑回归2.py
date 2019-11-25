from __future__ import print_function
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
y = np.array([0, 0, 1, 1, 1, 0])
plt.scatter(X,y,c="red")
plt.show()
lr = LogisticRegression()
lr.fit(X, y)
score = lr.score(X, y)
print("Score: %s" % score)
