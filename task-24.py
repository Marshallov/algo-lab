from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) 
        return self.parent[i]

    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = []            
        self.tree = defaultdict(list) 

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def build_mst(self):
        self.edges.sort()
        dsu = DSU(self.n)
        for w, u, v in self.edges:
            if dsu.union(u, v):
                self.tree[u].append((v, w))
                self.tree[v].append((u, w))

    def _find_path(self, u, target, parent=-1):
        if u == target:
            return [] 
            
        for v, w in self.tree[u]:
            if v != parent: 
                path = self._find_path(v, target, u)
                if path is not None:
                    return path + [(u, v, w)] 
        return None

    def is_still_mst(self, u, v, new_weight):
        path = self._find_path(u, v)
        max_edge = max(path, key=lambda edge: edge[2]) 
        
        return new_weight >= max_edge[2]

    def update_mst(self, u, v, new_weight):
        path = self._find_path(u, v)
        max_u, max_v, max_w = max(path, key=lambda edge: edge[2])

        if new_weight < max_w:
            self.tree[max_u].remove((max_v, max_w))
            self.tree[max_v].remove((max_u, max_w))
            self.tree[u].append((v, new_weight))
            self.tree[v].append((u, new_weight))
            
        new_mst_edges = set()
        for node in self.tree:
            for neighbor, weight in self.tree[node]:
                edge = (min(node, neighbor), max(node, neighbor), weight)
                new_mst_edges.add(edge)
                
        return list(new_mst_edges)




g = Graph(4)

g.add_edge(0, 1, 1)
g.add_edge(1, 2, 4)
g.add_edge(2, 3, 5)
g.add_edge(0, 2, 10) # Это "плохое" ребро, в MST оно не пойдет

# Строим изначальное дерево T
g.build_mst()
print("Изначальное дерево T было построено.\n")

# 2. Добавляем новое ребро (u=0, v=3, weight=2)
u, v, w = 0, 3, 2
print(f"Пытаемся добавить новое ребро: ({u} - {v}) с весом {w}")

# Пункт (a) - проверяем
is_optimal = g.is_still_mst(u, v, w)
print(f"(a) Остается ли старое дерево минимальным? Ответ: {is_optimal}")

# Пункт (b) - обновляем и выводим
if not is_optimal:
    print("(b) Дерево больше не оптимально. Запускаем обновление...")
    
new_tree_edges = g.update_mst(u, v, w)

print("\nНовое минимальное остовное дерево T (узел1, узел2, вес):")
for edge in sorted(new_tree_edges):
    print(edge)
