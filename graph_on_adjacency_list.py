import numpy as np
from graphviz import Graph
import string


class AdjMatrixGraph:
    def __init__(self):
        self.adj = np.zeros((0, 0))  # Матрица смежности
        self.attributes = list()  # Список атрибутов вершин, list of dict

    def add_vertices(self, n):
        """ Добавить n вершн в граф.

        :param int n: колиичество вершин для добавления
        """
        self.adj = self.enlarge_matrix(self.adj, n)
        for i in range(n):
            self.attributes.append(dict())

    def enlarge_matrix(self, a, n):
        """ Добавляет с правого и нижнего края матрицы n столбцов и n строк с
        нулями

        :param np.array a: матрица
        :param int n: количество строк/столбцов для добавления
        :return: результат добавления
        :rtype: np.array
        """
        cols, rows = a.shape
        return np.hstack((np.vstack((a, np.zeros((n, cols)))),
                          np.zeros((rows + n, n))))

    def remove_vertex(self, v):
        """ Удалить вершину из графа

        :param int v: индекс вершинаы графа
        """
        self.adj = np.delete(np.delete(self.adj, v, 1), v, 0)
        self.attributes.pop(v)

    def number_of_vertices(self):
        """ Возвращает количество вершин графа

        :rtype: int
        """
        return len(self.attributes)

    def add_edge(self, u, v):
        """ Добавить ребро, соединяющее вершины с индексами u и v

        :param int u: индекс вершины графа
        :param int v: индекс вершины графа
        """
        self.adj[u][v] = 1

    def remove_edge(self, u, v):
        """ Удалить ребро, соединяющее вершины с индексами u и v

        :param int u: индекс вершины графа
        :param int v: индекс вершины графа
        """
        self.adj[u][v] = 0

    def number_of_edges(self):
        """ Возвращает количество ребер в графе

        :rtype: int
        """
        num = 0
        for i in range(len(self.adj)):
            for j in range(len(self.adj[i])):
                num += self.adj[i][j]
        return int(num)

    def neighbors(self, v):
        """ Возвращает список индексов вершин, соседних с данной

        :param int v: индекс вершины графа
        :rtype: list of int
        """
        lst = []
        for i in range(len(self.adj[v])):
            if self.adj[v][i] == 0:
                continue
            else:
                lst.append(i)
        return lst

    def draw(self, filename='test.gv'):
        """
        Отрисовывает граф используя библиотеку Graphviz. Больше примеров:
        https://graphviz.readthedocs.io/en/stable/examples.html
        """
        g = Graph('G', filename=filename, engine='sfdp')

        for v, attr in enumerate(self.attributes):
            if 'color' in attr:
                g.attr('node', style='filled', fillcolor=attr['color'])
                if attr['color'] == 'black':
                    g.attr('node', fontcolor='white')
            else:
                g.attr('node', style='', color='', fontcolor='', fillcolor='')

            if 'name' in attr:
                g.node(str(v), label='{} ({})'.format(attr['name'], v))
            else:
                g.node(str(v))

        for i in range(self.number_of_vertices()):
            for j in range(i, self.number_of_vertices()):
                if self.adj[i][j]:
                    g.edge(str(i), str(j))

        g.view()
