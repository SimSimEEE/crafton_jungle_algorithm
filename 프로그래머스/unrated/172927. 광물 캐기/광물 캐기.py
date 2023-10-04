def solution(picks, minerals):
    answer = 0
    
    m_dict = { "diamond": 0, "iron": 0, "stone": 0 }
    dict = {0: (1, 1, 1), 1: (5, 1, 1), 2: (25, 5, 1)}
    
    results = []
    ln = sum(picks) * 5
    if len(minerals) > ln:
        minerals = minerals[:ln]
    for i, mineral in enumerate(minerals):
        m_dict[mineral] += 1
        if (i + 1) % 5 == 0:
            results.append([m_dict["diamond"], m_dict["iron"], m_dict["stone"]])
            m_dict["diamond"], m_dict["iron"], m_dict["stone"] = 0, 0, 0
    else:
        results.append([m_dict["diamond"], m_dict["iron"], m_dict["stone"]])
    results.sort(key = lambda x : -(dict[2][0] * x[0] + dict[2][1] * x[1] + dict[2][2] * x[2]))
    
    dia, iron, stone = picks
    for result in results:
        if dia:
            answer += dict[0][0] * result[0] + dict[0][1] * result[1] + dict[0][2] * result[2]
            dia -= 1
        elif iron:
            answer += dict[1][0] * result[0] + dict[1][1] * result[1] + dict[1][2] * result[2]
            iron -= 1
        elif stone:
            answer += dict[2][0] * result[0] + dict[2][1] * result[1] + dict[2][2] * result[2]
            stone -= 1
            
    return answer