def solution(arrows):
    direction = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    crnt_location = (0, 0)
    vertices = set({crnt_location})
    edges = set()

    for arrow in arrows:
        for _ in range(2):
            dx, dy = direction[arrow]
            new_location = (crnt_location[0] + dx, crnt_location[1] + dy)
            vertices.add(new_location)
            edges.add((new_location[0] + crnt_location[0], new_location[1] + crnt_location[1]))
            crnt_location = new_location

    return 1 - len(vertices) + len(edges)