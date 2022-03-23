# 넘파이: 수치 데이터를 처리하는 라이브러리이다. 넘파이가 제공하는 ndarray 배열은 순수 파이썬의
# 리스트에 비하여 아주 빠른 속도를 제공한다. 넘파이는 벡터 및 행렬, 선형 대수 연산을 지원한다.
# 딥러닝에서는 넘파이 배열을 이용하여 데이터 세트나 신경망의 가중치, 바이어스 등을 표현한다.
# 아나콘다에는 기본적으로 포함되어 있다.
# 맷플롯립(Matplotlib)  다양한 그래프를 그리는 라이브러리
# 사이킷런(Scikit-learn)    전통적인 머신러닝 라이브러리
# 텐서플로우(TensorFlow) 딥러닝을 지원하는 라이브러리
# 케라스(Keras)        고수준의 딥러닝 라이브러리
# 파이토치(PyTorch)     페이스북에서 만든 딥러닝 라이브러리
# 판다스(Pandas)       데이터 처리를 위한 라이브러리

import numpy as np
a = np.array([[0,1,2],
              [3,4,5],
              [6,7,8]])

a.shape     # 배열의 형상 (3,3)
a.ndim      # 배열의 차원 개수 2
a.dtype     # 요소의 자료형 dtype('int32')
a.itemsize  # 요소 한개의 크기 8
a.size      # 전체 요소의 개수 9

np.linspace(start, stop, num)   # 균일한 간격의 값으로 배열 생성하기
                                # linspace()는 시작값부터 끝값까지 균일한 간격으로 지정된 개수만큼의 배열을 생성

#np.newaxis 및 np.expand_dims을 사용하여 기존 배열의 크기를 증가시킬 수 있다. np.newaxis을 사용할 때마다 배열의 차원이 1차원 증가한다.

new_array = old_array.reshape((2,3))    # 배열의 형태 변경하기 2,3 >> 새로운 배열의 형상

a = np.random.rand(5,3)     # 균일 분포 난수 생성하기 5 >> 행의 개수 3 >> 열의 개수


a = np.random.normal(loc=0.0, scale=1.0, size=None) # loc 평균 scale 표준편차 size 배열의 차원
np.unique                   # 사용 시 배열에서 고유한 요소를 쉽게 찾을 수 있다.

# 맵플롯립 - 직선그래프
import matplotlib.pyplot as plt
%matplotlib inline

X=["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
Y1=[15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
Y2=[20.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.3]

plt.plot(X,Y1,label="Seoul")
plt.plot(X,Y2,label="Busan")
plt.xlabel("day")
plt.ylabel("temperature")
plt.legend(loc="upper left")
plt.title("Temperatures of Cities")
plt.show()
