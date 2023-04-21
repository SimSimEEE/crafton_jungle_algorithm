import sys
input = sys.stdin.readline

N = int(input())
nodes = dict()
for _ in range(N):
    root, left_child, right_child = input().split()
    nodes[root] = [left_child, right_child]

def pre_order(node):
    if node == '.':
        return
    print(node,end='')
    pre_order(nodes[node][0])
    pre_order(nodes[node][-1])

def in_order(node):
    if node == '.':
        return
    in_order(nodes[node][0])
    print(node,end='')
    in_order(nodes[node][-1])

def post_order(node):
    if node == '.':
        return
    post_order(nodes[node][0])
    post_order(nodes[node][-1])
    print(node,end='')
    

pre_order('A')
print()
in_order('A')
print()
post_order('A')