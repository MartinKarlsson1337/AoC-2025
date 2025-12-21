
class Node:
    def __init__(self, row: str):
        row = row.strip()
        self.name = row.split(':')[0]
        self.neighbours = row.split(' ')[1:]
        

def count_paths(graph, src, dest, visited):
    if src == dest:
        return 1

    visited.add(src)
    total = 0

    for nxt in graph.get(src, []):
        if nxt not in visited:
            total += count_paths(graph, nxt, dest, visited)

    visited.remove(src)
    return total



if __name__ == '__main__':
    with open('day11/day11.txt', 'r') as f:
        data = f.readlines()

    num_of_nodes = len(data) + 1

    nodes = [Node(row) for row in data]

    graph = {node.name: node.neighbours for node in nodes}

    paths = count_paths(graph, 'you', 'out', set())
    print(paths)


