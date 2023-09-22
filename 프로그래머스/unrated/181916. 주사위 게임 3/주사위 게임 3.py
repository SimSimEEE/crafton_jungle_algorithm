def solution(a, b, c, d):
    answer = 0
    dice = [0] * 7
    for i in [a, b, c, d]:
        dice[i] += 1
    if 4 in dice:
        return a * 1111
    elif 3 in dice:
        return (10 * dice.index(3) + dice.index(1)) ** 2
    elif 2 in dice and not 1 in dice:
        return abs(dice.index(2)**2 - a*b*c*d//dice.index(2)**2)
    elif 2 in dice:
        return a*b*c*d//dice.index(2)**2
    else:
        return min([a, b, c, d])
    return answer