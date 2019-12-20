from sklearn import svm


def createDataSet(fileName):
  x = []
  y = []
  with open(fileName) as fr:
    for line in fr.readlines():
      lineArr = line.strip().split(' ')
      x.append([float(lineArr[0]), float(lineArr[1])])
      y.append(float(lineArr[2]))
  return x, y


dataset, labels = createDataSet('testSet.txt')
train_len = int(len(labels)-1)
train_dataset = dataset[:train_len]
train_labels = labels[:train_len]
valid_dataset = [[8.6, 4.0001]]
clf = svm.SVC(C=10000.0, kernel='rbf')
clf.fit(train_dataset, train_labels)
predictions = [int(a) for a in clf.predict(valid_dataset)]
print(predictions)


