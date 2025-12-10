from typing import List
# __matmul__ Magic Method를 이용해 W @ T 행렬 내적을 계산하는 예제
# Magic Method 관점에서 구현 및 동작 절차를 설명해라

class Tensor:

   def __init__(self, data: List[List[float]]) -> None:
      self.data = data

   def __matmul__(self, other):
      A = self.data
      B = other.data

      # self (A 행렬): N X K
      N = len(A)
      K = len(A[0])

      # other (B 행렬): K X M
      M = len(B[0])

      # 결과 행렬 초기화
      result_data = [[0.0] * M for _ in range(N)]

      for i in range(N):
         for j in range(M):
            for k in range(K):
               result_data[i][j] += A[i][k] * B[k][j]
      
      return Tensor(result_data)
   
   def __repr__(self) -> str:
      return f"Tensor ({self.data})"


W = Tensor([[1.0, 2.0], [3.0, 4.0]])

T = Tensor([[5.0], [6.0]])

R = W @ T

print(R)