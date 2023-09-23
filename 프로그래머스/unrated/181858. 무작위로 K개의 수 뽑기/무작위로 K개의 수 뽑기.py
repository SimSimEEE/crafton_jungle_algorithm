def solution(arr, k):
    unique_elements = []
    result = []
    
    for elem in arr:
        if elem not in unique_elements:
            unique_elements.append(elem)
            result.append(elem)
            if len(result) == k:
                return result
    
    result += [-1] * (k - len(result))
    return result
