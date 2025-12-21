from functools import lru_cache
from tqdm import tqdm

from collections import defaultdict, deque


class Node:
    def __init__(self, row: str):
        row = row.strip()
        self.name = row.split(':')[0]
        self.neighbours = row.split(' ')[1:]
        

def reverse_graph(G):
    R = defaultdict(list)
    for u in G:
        for v in G[u]:
            R[v].append(u)
    return R

def reachable_from(G, start):
    seen = set()
    stack = [start]
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        stack.extend(G[u])
    return seen


def count_simple_paths(graph, src, dest):
    nodes = list(graph.keys())
    idx = {n: i for i, n in enumerate(nodes)}

    pbar = tqdm(desc="DFS states evaluated")

    @lru_cache(None)
    def dfs(u, visited_mask):
        pbar.update(1)

        if u == dest:
            return 1

        total = 0
        for v in graph[u]:
            bit = 1 << idx[v]
            if not (visited_mask & bit):
                total += dfs(v, visited_mask | bit)
        return total

    result = dfs(src, 1 << idx[src])
    pbar.close()
    return result


def count_paths_via_fft_and_dac(G):
    GR = reverse_graph(G)

    can_reach_out = reachable_from(GR, "out")
    can_reach_dac = reachable_from(GR, "dac")
    can_reach_fft = reachable_from(GR, "fft")

    G1 = {u: [v for v in G[u] if v in can_reach_fft]
          for u in G if u in can_reach_fft}

    G2 = {u: [v for v in G[u] if v in can_reach_dac]
          for u in G if u in can_reach_dac}

    G3 = {u: [v for v in G[u] if v in can_reach_out]
          for u in G if u in can_reach_out}

    # Count each segment
    c1 = count_simple_paths(G1, "svr", "fft")
    c2 = count_simple_paths(G2, "fft", "dac")
    c3 = count_simple_paths(G3, "dac", "out")

    return c1 * c2 * c3


if __name__ == '__main__':
    with open('day11/day11.txt', 'r') as f:
        data = f.readlines()

    num_of_nodes = len(data) + 1

    nodes = [Node(row) for row in data]

    graph = {node.name: node.neighbours for node in nodes}
    graph.update({"out": []})

    paths = count_paths_via_fft_and_dac(graph)
    print(paths)


