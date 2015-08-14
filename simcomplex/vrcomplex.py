__author__ = 'stephenhky'

from simcomplex import SimplicialComplex
import networkx as nx
from scipy.spatial import distance
from itertools import product

class VietorisRipsComplex(SimplicialComplex):
    def __init__(self, points, epsilon, labels=None, distfcn=distance.euclidean):
        self.pts = points
        self.labels = range(len(self.pts)) if labels==None or len(labels)!=len(self.pts) else labels
        self.epsilon = epsilon
        self.distfcn = distfcn
        self.network = self.construct_network(self.pts, self.labels, self.epsilon, self.distfcn)
        self.import_simplices(map(tuple, list(nx.find_cliques(self.network))))

    def construct_network(self, points, labels, epsilon, distfcn):
        g = nx.Graph()
        g.add_nodes_from(labels)
        zips = zip(points, labels)
        for pair in product(zips, zips):
            if pair[0][1]!=pair[1][1]:
                dist = distfcn(pair[0][0], pair[1][0])
                if dist<epsilon:
                    g.add_edge(pair[0][1], pair[1][1])
        return g