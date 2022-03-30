import matplotlib.pyplot as plt

from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=6)

X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.2) # 데이터 분할

knn.fit(X_train, y_train) # train
y_pred = knn.predict(X_test)  # 예측

disp = metrics.plot_confusion_matrix(knn, X_test, y_test)
plt.show()