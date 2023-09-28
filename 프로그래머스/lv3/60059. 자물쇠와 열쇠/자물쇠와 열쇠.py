def rotate(key):
    return list(zip(*key[::-1]))

def padding(M, N):
    zeros = [[0 for _ in range(N)] for _ in range(N)]
    pad_ud = [[0 for _ in range(N+(M-1)*2)] for _ in range(M-1)]
    pad_lr = [0 for _ in range(M-1)]
    return pad_ud + [pad_lr+row+pad_lr for row in zeros] + pad_ud

def check(key, lock):
    if key == [[1 if v == 0 else 0 for v in row] for row in lock]:
        return True
    return False

def slide(i, j, M, pad_N):
    if j < pad_N - M:
        return i, j+1
    elif i < pad_N - M:
        return i+1, 0
    else:
        return -1, -1

def merge(pad_key, key, i, j):
    copy_key = pad_key[:]
    for row in range(len(pad_key)):
        if not i <= row < i+len(key): continue
        for col in range(len(pad_key)):
            if not j <= col < j+len(key): continue
            copy_key[row][col] = key[row-i][col-j]
    return copy_key

def solution(key, lock):
    M, N = len(key), len(lock)
    for _ in range(4):
        i, j = 0, 0
        while i >= 0 and j >= 0:
            sub_key = merge(padding(M, N), key, i, j)
            if check([row[M:M+N] for row in sub_key[M:M+N]], lock):
                return True
            i, j = slide(i, j, len(key), len(sub_key))
        key = rotate(key)
    return False