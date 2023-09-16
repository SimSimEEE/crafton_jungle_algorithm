import math
def solution(arrayA, arrayB):
    gcdA, gcdB = 0, 0
    for A in arrayA:
        gcdA = math.gcd(gcdA, A)
    for B in arrayB:
        gcdB = math.gcd(gcdB, B)
    for B in arrayB:
        if B%gcdA == 0:
            gcdA = 0
            break
    for A in arrayA:
        if A%gcdB == 0:
            gcdB = 0
            break
    return max(gcdA, gcdB)