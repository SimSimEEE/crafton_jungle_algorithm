zoac = list(map(str, input()))
result = [''] * len(zoac)

def zoac_print(zoac, start):
    global result
    if not zoac:
        return
    target = min(zoac)
    i = zoac.index(target)
    result[start + i] = target
    print(''.join(result))
    zoac_print(zoac[i + 1:], start + i + 1)
    zoac_print(zoac[:i], start)
    
zoac_print(zoac, 0)