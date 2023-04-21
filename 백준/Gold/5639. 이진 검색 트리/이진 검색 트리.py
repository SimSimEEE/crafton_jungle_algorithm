import sys
sys.setrecursionlimit(10**6)
lines = sys.stdin.readlines()
nodes = []
for line in lines:
    nodes.append(int(line))

def pre_to_post_order(nodes):
    if len(nodes) == 0:
        return
    left, right = [],[]
    root = nodes[0]
    for node in nodes:
        if node < root:
            left.append(node)
        elif node > root:
            right.append(node)
    pre_to_post_order(left)
    pre_to_post_order(right)
    print(root)

pre_to_post_order(nodes)