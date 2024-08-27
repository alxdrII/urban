import math
from pprint import pprint


class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1:Vertex, v2:Vertex, dist=1):
        # ??? ..добавим новую связь в список связей у вершины.. ???
        # но тогда при создании образцов для поиска, будут запоминатся временные, ненужные связи!
        v1.links.append(self)
        v2.links.append(self)

        self._v1 = v1
        self._v2 = v2
        self._dist = dist

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value

    def __eq__(self, other):
        return (self.v1 == other.v1 or self.v1 == other.v2) \
            and (self.v2 == other.v1 or self.v2 == other.v2) # and self.dist == other.dist

    def __hash__(self):
        return hash((hash(self.v1) * hash(self.v2))) # , self.dist))

    def __repr__(self):
        return f"l-{self.dist}"


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        if dist <= 0:
            raise ValueError('расстояние между станциями должно быть положительным')
        super().__init__(v1, v2, dist)


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v:Vertex):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link:Link):
        if link not in self._links:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

            # # добавляем связь в список связей вершин
            # if link not in link.v1.links:
            #     link.v1.links.append(link)
            # if link not in link.v2.links:
            #     link.v2.links.append(link)

    # def get_link_dist(self, v1:Vertex, v2:Vertex):
    #     """находит имеющуюся связь между двумя вершинами и возвращает рассотяние между ними
    #        если прямой связи нет, то возвращает бесконечность"""
    #
    #     res = math.inf
    #     links_v1 = [ln for ln in v1.links if ln]
    #     return 0
    #

    def find_path(self, start_v, stop_v):
        """Возвращает список из вершин кратчайшего маршрута и список из связей этого же маршрута в виде кортежа"""

        def find_lowest_cost_node(costs):
            lowest_cost = math.inf
            lowest_cost_node = None
            for node in costs:   # перебрать все вершины
                cost = costs[node]
                if cost < lowest_cost and node not in processed:
                    lowest_cost = cost
                    lowest_cost_node = node

            return lowest_cost_node

        graph = {} # хранится полный список вершин с соседями и весами
        for v in self._vertex:
            graph[v] = {}
            for l in v.links:
                graph[v][l.v1 if l.v1 != v else l.v2] = l.dist

        costs = {} # таблица стоимостей
        for l in start_v.links:
            costs[l.v1 if l.v1 != start_v else l.v2] = l.dist
        costs[stop_v] = math.inf

        parents = {}  # хеш-таблица родителей
        for l in start_v.links:
            parents[l.v1 if l.v1 != start_v else l.v2] = start_v
        parents[stop_v] = None

        processed = [] # отслеживание отработанных процессов

        node = find_lowest_cost_node(costs)
        while node is not None: # пока не обработаны все вершины
            cost = costs[node]
            neighbors = graph[node]
            for n in neighbors.keys(): # перебрать всех соседей текущей вершины
                new_cost = cost + neighbors[n]
                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = node

            processed.append(node)
            node = find_lowest_cost_node(costs)

        return parents, costs


map_graph = LinkedGraph()

v1 = Station("v1")
v2 = Station("v2")
v3 = Station("v3")
v4 = Station("v4")
v5 = Station("v5")
v6 = Station("v6")
v7 = Station("v7")

# map_graph.add_link(Link(v1, v2))
# map_graph.add_link(Link(v2, v3))
# map_graph.add_link(Link(v1, v3))
#
# map_graph.add_link(Link(v4, v5))
# map_graph.add_link(Link(v6, v7))
#
# map_graph.add_link(Link(v2, v7))
# map_graph.add_link(Link(v3, v4))
# map_graph.add_link(Link(v5, v6))

map_graph.add_link(Link(v1, v2, 3))
map_graph.add_link(Link(v1, v3, 1))
map_graph.add_link(Link(v1, v4, 3))

map_graph.add_link(Link(v2, v3, 4))
map_graph.add_link(Link(v4, v6, 2))
map_graph.add_link(Link(v6, v3, 5))

map_graph.add_link(Link(v6, v5, 4))
map_graph.add_link(Link(v3, v5, 7))
map_graph.add_link(Link(v3, v7, 11))

print(len(map_graph._links))   # 9 связей
print(len(map_graph._vertex))  # 7 вершин
path = map_graph.find_path(v1, v5)
pprint(path)

# print("v1", v1.links)
# print("v2", v2.links)
# print("v3", v3.links)
# print("v4", v4.links)
# print("v5", v5.links)
# print("v6", v6.links)
# print("v7", v7.links)

# -----------------
# map_metro = LinkedGraph()
# v1 = Station("Сретенский бульвар")
# v2 = Station("Тургеневская")
# v3 = Station("Чистые пруды")
# v4 = Station("Лубянка")
# v5 = Station("Кузнецкий мост")
# v6 = Station("Китай-город 1")
# v7 = Station("Китай-город 2")
#
# map_metro.add_link(LinkMetro(v1, v2, 1))
# map_metro.add_link(LinkMetro(v2, v3, 1))
# map_metro.add_link(LinkMetro(v1, v3, 1))
#
# map_metro.add_link(LinkMetro(v4, v5, 1))
# map_metro.add_link(LinkMetro(v6, v7, 1))
#
# map_metro.add_link(LinkMetro(v2, v7, 5))
# map_metro.add_link(LinkMetro(v3, v4, 3))
# map_metro.add_link(LinkMetro(v5, v6, 3))
#
# print(len(map_metro._links))
# print(len(map_metro._vertex))
# path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
# print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
# print(sum([x.dist for x in path[1]]))  # 7
