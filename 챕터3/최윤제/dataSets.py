import matplotlib.pyplot as plt

from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()   # 데이터 세트를 불러온다
plt.imshow(digits.images[0], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1)) # 평탄화

from sklearn.neighbors import KNeighborsClassifier # knn 알고리즘

knn = KNeighborsClassifier(n_neighbors=6)

X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.2) # 데이터 분할

knn.fit(X_train, y_train) # train

y_pred = knn.predict(X_test)  # 예측

scores = metrics.accuracy_score(y_test, y_pred) # 정확도 계산
print(scores)

plt.imshow(X_test[10].reshape(8,8), cmap=plt.cm.gray_r, interpolation='nearest') # 이미지 8*8로 변경후 다시 출력
plt.show()

y_pred = knn.predict([X_test[10]])
print(y_pred)
