class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


def kruskal(edges):
    edges.sort()  # 간선을 가중치 순으로 정렬
    mst_edges = []  # 최소 신장 트리의 간선 목록
    num_vertices = len(set([u for _, u, _ in edges]).union(
        set([v for _, _, v in edges])))
    uf = UnionFind(num_vertices)

    for edge in edges:
        weight, u, v = edge

        if uf.find(u) != uf.find(v):  # 사이클이 아닌 경우에만 추가
            uf.union(u, v)
            mst_edges.append(edge)

    return mst_edges


# 예시 입력: (숫자, 알파벳 대문자, 알파벳 대문자)로 구성된 간선 목록
edges = [(7, 'A', 'B'), (5, 'A', 'C'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'C', 'D'),
         (5, 'C', 'E'), (15, 'D', 'E'), (6, 'D', 'F'), (8, 'E', 'F')]

mst_edges = kruskal(edges)
print("Minimum Spanning Tree Edges:")
for edge in mst_edges:
    print(edge)
