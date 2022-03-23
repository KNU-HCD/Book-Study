import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9]) # 배열 생성
b = np.array([[1,2,3], [4,5,6]]) # 2차원 배열 행렬에 형태를 가진다.

b.ndim # 축의 개수
b.shape # 행과 열의 수
b.size # 배열 안에 있는 요소들의 총 개수
b.dtype # 자료형 확인

np.zeros((3,4)) # 행이3이고 열이 4인 0으로 가득찬 행렬생성
np.ones((3, 4), dtype=np.int32) # 1로 가득찬 배열

np.arange(5) # 0~4까지 배열에 저장
np.arange(1, 6) # 1~6까지 배열에 저장
np.arange(1, 10, 3) # 1~10까지 간격이 3으로 배열에 저장
#print(np.arange(1, 10, 3))

np.linspace(0, 10, 100) # 0에서 10사이에 수들을 균일하게 100개 만든다.
np.sort(a) #정렬

x = np.array([[1, 2],[3, 4]])
y = np.array([[5, 6],[7, 8]])

np.concatenate((x, y), axis=1) # 배열 합치기 axis는 합치는 축 지정
np.vstack((x, y)) # 수직으로 스택쌓기
np.hstack((x, y)) # 가로로 스택쌓기

a.reshape(3, 3) # 3행과 3열인 2차원 배열로 변경
# a.reshape(6, -1) # 행의 개수는 6개이고 열의 개수는 데이터의 개수에 맞춰서 결정된다.

array = np.arange(30).reshape(-1, 10) # 열의 개수 10개로 하고 행은 맞춰서 0~30개 배열 만든다.
arr1, arr2 = np.split(array, [3], axis=1) # array[3] 기준으로 세로로 자른다 axis가 0이면 가로로

a[np.newaxis, :] # 배열의 차원 증가

ages = np.array([18, 19, 25, 30, 28])
ages[1:3] # 문자열 슬라이스 인덱스 1~2까지 슬라이스
ages[0:3] # 0~2까지 슬라이스

data = np.array([[1,2,3],[4, 5, 6],[7,8,9]])
data[0:2, 1:3] # 행 0~1까지 열 1~1까지 슬라이싱
data[::2, ::2] # 시작과 끝까지 간격을 2로 슬라이스

data.mean(axis=0) # 각 열에서 모든 행값의 평균을 구한다! ex) 147 258 369 의 편균을 구하는것
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = np.array([[2,2,2],[2,2,2],[2,2,2]])

result = arr1 * arr2 # 곱하고 더하고 다가능
result2 = arr1 @ arr2 # 행렬곱셈이 가능하다

np.random.seed(100) # seed설정
np.random.rand(5) # 랜덤값5개
np.random.rand(5, 3) # 랜덤값 행5 열3

a1, a2 = 10, 20
(a2-a1)*np.random.rand(5)+a1 # 10~20사이에 난수 5개 생성
np.random.randint(1, 7, size=10) #정수 생성
np.random.normal(0, 0.1, 5) # 평균이 0이고 표준편차가 0.1인 5개 난수생성

np.unique(a) # 겹치는거 다 제거

b.T # T는 전치연산
b.flatten() # 다차원 배열 1차원으로