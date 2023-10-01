def solution(cards):
    answer = 0
    for i, card in enumerate(cards):
        visited = [False] * len(cards)
        idx = i
        first_box = 0
        while not visited[idx]:
            visited[idx] = True
            idx = cards[idx] - 1
            first_box += 1
        if idx == len(cards):
            continue
        for i, e in enumerate(visited):
            if not e:
                visited2 = [False] * len(cards)
                idx = i
                second_box = 0
                while not e and not visited2[idx]:
                    visited2[idx] = True
                    idx = cards[idx] - 1
                    second_box += 1
                answer = max(answer, first_box * second_box)
    return answer