import numpy as np

def is_node_part_of_circuit(adj: np.ndarray, node: int) -> bool:
    return (adj[node] != -1).sum() > 1

def is_node_unconnected(adj: np.ndarray, node: int) -> bool:
    return (adj[node] != -1).sum() == 1

def get_circuit_id(adj: np.ndarray, node: int) -> int:
    row = adj[node]
    ids = np.unique(row[row != -1])
    return int(ids.max())   # ← FIX: take most recent circuit ID

def get_nodes_in_circuit(adj: np.ndarray, cid: int) -> np.ndarray:
    diag = adj.diagonal()
    return np.where(diag == cid)[0]

def connect(adj: np.ndarray, node1: int, node2: int) -> None:
    cid1 = get_circuit_id(adj, node1)
    cid2 = get_circuit_id(adj, node2)

    if cid1 == cid2:
        return

    if is_node_unconnected(adj, node1) and is_node_unconnected(adj, node2):
        adj[node1, node2] = node1
        adj[node2, node1] = node1
        adj[node2, node2] = node1
        return

    if is_node_part_of_circuit(adj, node1) and is_node_unconnected(adj, node2):
        adj[node1, node2] = cid1
        adj[node2, node1] = cid1
        adj[node2, node2] = cid1
        return

    if is_node_part_of_circuit(adj, node2) and is_node_unconnected(adj, node1):
        adj[node1, node2] = cid2
        adj[node2, node1] = cid2
        adj[node1, node1] = cid2
        return

    if is_node_part_of_circuit(adj, node1) and is_node_part_of_circuit(adj, node2):
        nodes_c2 = get_nodes_in_circuit(adj, cid2)
        for n in nodes_c2:
            adj[n, adj[n] != -1] = cid1
            adj[adj[:, n] != -1, n] = cid1
            adj[n, n] = cid1
        return

    print("Unexpected condition!")


if __name__ == '__main__':
    data = np.loadtxt("day8/day8.txt", delimiter=",", dtype=np.int64)

    diffs = data[:, None, :] - data[None, :, :]
    distances = np.sqrt((diffs ** 2).sum(axis=2))
    distances[distances == 0] = np.inf

    adj = np.zeros_like(distances, dtype=np.int64) - 1
    adj[distances == np.inf] = np.arange(adj.shape[0])

    i, j = np.triu_indices(len(data), 1)
    pair_distances = distances[i, j]
    order = np.argsort(pair_distances)
    pairs = list(zip(i[order], j[order]))

    last_connection = None

    for r, c in pairs:
        connect(adj, int(r), int(c))

        diag = adj.diagonal()
        if np.all(diag == diag[0]):
            last_connection = (r, c)
            break

    result = data[last_connection[0]][0] * data[last_connection[1]][0]
    print(result)
