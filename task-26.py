def find_road_network(n, k, anaza_edges, bani_yas_edges):
    class DSU:
        def __init__(self, size):
            self.parent = list(range(size))
            self.rank = [0] * size
            self.components = size

        def find(self, i):
            if self.parent[i] == i:
                return i
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

        def union(self, i, j):
            root_i = self.find(i)
            root_j = self.find(j)
            if root_i != root_j:
                if self.rank[root_i] < self.rank[root_j]:
                    self.parent[root_i] = root_j
                elif self.rank[root_i] > self.rank[root_j]:
                    self.parent[root_j] = root_i
                else:
                    self.parent[root_j] = root_i
                    self.rank[root_i] += 1
                self.components -= 1
                return True
            return False

    dsu_min = DSU(n)
    for u, v in bani_yas_edges:
        dsu_min.union(u, v)

    essential_anaza_idx = set()
    for i, (u, v) in enumerate(anaza_edges):
        if dsu_min.union(u, v):
            essential_anaza_idx.add(i)

    if dsu_min.components > 1:
        return None

    min_k = len(essential_anaza_idx)

    dsu_max = DSU(n)
    max_k = 0
    for u, v in anaza_edges:
        if dsu_max.union(u, v):
            max_k += 1

    if not (min_k <= k <= max_k):
        return None

    dsu_res = DSU(n)
    result = []

    for i in essential_anaza_idx:
        u, v = anaza_edges[i]
        dsu_res.union(u, v)
        result.append((u, v, 'Аназа'))

    needed_anaza = k - min_k
    for i, (u, v) in enumerate(anaza_edges):
        if needed_anaza == 0:
            break
        if i not in essential_anaza_idx:
            if dsu_res.union(u, v):
                result.append((u, v, 'Аназа'))
                needed_anaza -= 1

    for u, v in bani_yas_edges:
        if dsu_res.union(u, v):
            result.append((u, v, 'Бани Яс'))

    return tuple(result)

# Пример 1

n_1 = 4
k_1 = 2
anaza_edges_1 = [(0, 1), (1, 2), (2, 3)]
bani_yas_edges_1 = [(0, 3), (0, 2)]

result_1 = find_road_network(n_1, k_1, anaza_edges_1, bani_yas_edges_1)
print(result_1)

# Пример 2

n_2 = 4
k_2 = 0
anaza_edges_2 = [(0, 1), (1, 2), (2, 3)]
bani_yas_edges_2 = [(0, 3), (0, 2)]

result_2 = find_road_network(n_2, k_2, anaza_edges_2, bani_yas_edges_2)
print(result_2)

# Пример 3

n_3 = 5
k_3 = 2
anaza_edges_3 = [(0, 1), (1, 2)]
bani_yas_edges_3 = [(2, 3), (0, 3)]

result_3 = find_road_network(n_3, k_3, anaza_edges_3, bani_yas_edges_3)
print(result_3)