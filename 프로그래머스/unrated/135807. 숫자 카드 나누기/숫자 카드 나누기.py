import math
def calculate_gcd(arr):
    result = 0
    for num in arr:
        result = math.gcd(result, num)
    return result
def solution(arrayA, arrayB):
    gcdA = calculate_gcd(arrayA)
    gcdB = calculate_gcd(arrayB)
    if any(B % gcdA == 0 for B in arrayB):
        gcdA = 0
    if any(A % gcdB == 0 for A in arrayA):
        gcdB = 0
    return max(gcdA, gcdB)