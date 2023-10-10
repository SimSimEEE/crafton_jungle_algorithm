def solution(scores):
    wanho_work_attitude, wanho_peer_review = scores[0]
    other_scores = scores[1:]
    max_peer_review = 0
    rank = 1

    sorted_other_scores = sorted(other_scores, key=lambda s: (-s[0], s[1]))

    for other_work_attitude, other_peer_review in sorted_other_scores:
        if wanho_work_attitude < other_work_attitude and wanho_peer_review < other_peer_review:
            return -1

        if max_peer_review <= other_peer_review:
            max_peer_review = other_peer_review

            if wanho_work_attitude + wanho_peer_review < other_work_attitude + other_peer_review:
                rank += 1

    return rank
