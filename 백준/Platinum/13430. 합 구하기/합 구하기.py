k, n = map(int, input().split())
matrix = [[1]*i + [0]*(k+2-i) for i in range(1, k+3)]

def lower_triangular_matrix_multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]  # 결과 행렬 C를 초기화
    
    for i in range(n):
        for j in range(i + 1):  # 하삼각행렬이므로 j는 i 이하의 값만 고려합니다.
            if j <= i:
                for k in range(i + 1):
                    C[i][j] += A[i][k] * B[k][j]  # 요소 계산
    
    return C


def matrix_pow(A, n):
    if n == 1:
        return A
    
    result = [[1 if i == j else 0 for j in range(len(A))] for i in range(len(A))]  # 단위 행렬 초기화
    while n > 0:
        if n % 2 == 1:
            result = lower_triangular_matrix_multiply(result, A)
        A = lower_triangular_matrix_multiply(A, A)
        n //= 2
    
    return result


matrix = matrix_pow(matrix, n-1)

print(sum(matrix[-1]) % 1000000007)