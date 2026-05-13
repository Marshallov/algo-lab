from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.tree = defaultdict(list)

    def add_tree_edge(self, u, v, w):
        self.tree[u].append((v, w))
        self.tree[v].append((u, w))

    # Поиск максимального ребра на пути u -> v
    def max_edge_on_path(self, u, v):
        parent = [-1] * self.n
        edge_weight = [0] * self.n

        q = deque([u])
        parent[u] = u

        # BFS
        while q:
            cur = q.popleft()

            if cur == v:
                break

            for nxt, w in self.tree[cur]:
                if parent[nxt] == -1:
                    parent[nxt] = cur
                    edge_weight[nxt] = w
                    q.append(nxt)

        # Восстанавливаем путь и ищем max edge
        max_w = -1
        max_edge = None

        cur = v
        while cur != u:
            if edge_weight[cur] > max_w:
                max_w = edge_weight[cur]
                max_edge = (cur, parent[cur], edge_weight[cur])

            cur = parent[cur]

        return max_edge  

    # (a) Проверка: остается ли T MST
    def is_still_mst(self, u, v, new_weight):
        _, _, max_w = self.max_edge_on_path(u, v)

        return new_weight >= max_w

    # (b) Построение нового MST
    def update_mst(self, u, v, new_weight):
        a, b, max_w = self.max_edge_on_path(u, v)

        # Если новое ребро не улучшает MST
        if new_weight >= max_w:
            return

        # Удаляем тяжелое ребро
        self.tree[a] = [(x, w) for x, w in self.tree[a]
                        if not (x == b and w == max_w)]

        self.tree[b] = [(x, w) for x, w in self.tree[b]
                        if not (x == a and w == max_w)]

        # Добавляем новое ребро
        self.add_tree_edge(u, v, new_weight)



g = Graph(4)

# MST
g.add_tree_edge(0, 1, 1)
g.add_tree_edge(1, 2, 4)
g.add_tree_edge(2, 3, 5)

# Новое ребро
u, v, w = 0, 3, 2

# (a)
print(g.is_still_mst(u, v, w))

# (b)
g.update_mst(u, v, w)

print(dict(g.tree))