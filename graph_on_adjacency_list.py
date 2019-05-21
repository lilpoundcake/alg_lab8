#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from graphviz import Graph
import string


class AdjListGraph:
    def __init__(self):
        self.adj = list()  # Список смежности
        self.attributes = list()  # Список атрибутов вершин, list of dict

    def add_vertices(self, n):
        """ Добавить n вершн в граф.

        :param int n: колиичество вершин для добавления
        """
        for i in range(n):
            self.adj.append(list())
            self.attributes.append(dict())

    def remove_vertex(self, v):
        """ Удалить вершину из графа

        :param int v: индекс вершинаы графа
        """
        self.adj.pop(v)
        self.attributes.pop(v)

    def number_of_vertices(self):
        """ Возвращает количество вершин графа

        :rtype: int
        """
        return len(self.adj)

    def add_edge(self, u, v):
        """ Добавить ребро, соединяющее вершины с индексами u и v

        :param int u: индекс вершины графа
        :param int v: индекс вершины графа
        """
        #начал делать не так
        """self.adj[u], self.adj[v] = [u], [v]
        if u in self.attributes[u]:
            temp = self.attributes[u][u]
            temp.append(v)
            self.attributes[u][u] = temp
        else:
            self.attributes[u][u] = [v]
            
        if v in self.attributes[v]:
            temp = self.attributes[v][v]
            temp.append(u)
            self.attributes[v][v] = temp
        else:
            self.attributes[v][v] = [u]"""
        
        self.adj[u].append(v)
        self.adj[v].append(u)

    def remove_edge(self, u, v):
        """ Удалить ребро, соединяющее вершины с индексами u и v

        :param int u: индекс вершины графа
        :param int v: индекс вершины графа
        """
        self.adj[u].pop(v)
        self.adj[v].pop(u)
        
    def number_of_edges(self):
        """ Возвращает количество ребер в графе

        :rtype: int
        """
        num = 0
        for i in range(len(self.adj)):
            num += len(self.adj[i])
        return int(num/2)

    def neighbors(self, v):
        """ Возвращает список индексов вершин, соседних с данной

        :param int v: индекс вершины графа
        :rtype: list of int
        """
        return self.adj[v]

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
            for j in self.adj[i]:
                if i < j:
                    g.edge(str(i), str(j))

        g.view()

def main():
    g = AdjListGraph()
    g.add_vertices(5)
    for i, c in zip(range(5), string.ascii_lowercase):
        g.attributes[i]['name'] = c

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.remove_edge(1, 2)
    print(g.number_of_edges())
    print(g.number_of_vertices())
    print(g.neighbors(1))
    g.draw()


if __name__ == "__main__":
    main()
