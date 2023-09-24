def solution(rank, attendance):
    rank = sorted([[e,i] for i, e in enumerate(rank) if attendance[i]])
    return rank[0][1]*10000 + rank[1][1]*100 + rank[2][1]