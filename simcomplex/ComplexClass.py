__author__ = 'stephenhky'

from itertools import combinations
from scipy.sparse import dok_matrix
import numpy as np

class SimplicialComplex:
    def __init__(self, simplices=[]):
        self.import_simplices(simplices=simplices)

    def import_simplices(self, simplices=[]):
        self.simplices = map(lambda simplex: tuple(sorted(simplex)), simplices)
        self.face_set = self.faces()

    def faces(self):
        faceset = set()
        for simplex in self.simplices:
            numnodes = len(simplex)
            for r in range(numnodes, 0, -1):
                for face in combinations(simplex, r):
                    faceset.add(face)
        return faceset

    def n_faces(self, n):
        return filter(lambda face: len(face)==n+1, self.face_set)

    def boundary_operator(self, i):
        source_simplices = self.n_faces(i-1)
        target_simplices = self.n_faces(i-2)

        if len(target_simplices)==0:
            return dok_matrix((len(source_simplices), 0), dtype=np.float32)

        source_simplices_dict = {}
        for j in range(len(source_simplices)):
            source_simplices_dict[source_simplices[j]] = j
        target_simplices_dict = {}
        for i in range(len(target_simplices)):
            target_simplices_dict[target_simplices[i]] = i

        S = dok_matrix((len(target_simplices), len(source_simplices)), dtype=np.float32)
        for source_simplex in source_simplices:
            for a in range(len(source_simplex)):
                target_simplex = source_simplex[:a]+source_simplex[(a+1):]
                i = target_simplices_dict[target_simplex]
                j = source_simplices_dict[source_simplex]
                S[i, j] = (-1)**a

        return S