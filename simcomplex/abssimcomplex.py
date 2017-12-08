__author__ = 'stephenhky'

from scipy.sparse import dok_matrix
import numpy as np
from operator import add

from . import faces

class SimplicialComplex:
    def __init__(self, simplices=[]):
        self.import_simplices(simplices=simplices)

    def import_simplices(self, simplices=[]):
        self.simplices = map(lambda simplex: tuple(sorted(simplex)), simplices)
        self.face_set = faces(self.simplices)

    def n_faces(self, n):
        return filter(lambda face: len(face)==n+1, self.face_set)

    def boundary_operator(self, i):
        source_simplices = self.n_faces(i)
        target_simplices = self.n_faces(i-1)

        if len(target_simplices)==0:
            S = dok_matrix((1, len(source_simplices)), dtype=np.float64)
            S[0, 0:len(source_simplices)] = 1
        else:
            source_simplices_dict = {source_simplices[j]: j for j in range(len(source_simplices))}
            target_simplices_dict = {target_simplices[i]: i for i in range(len(target_simplices))}

            S = dok_matrix((len(target_simplices), len(source_simplices)), dtype=np.float64)
            for source_simplex in source_simplices:
                for a in range(len(source_simplex)):
                    target_simplex = source_simplex[:a]+source_simplex[(a+1):]
                    i = target_simplices_dict[target_simplex]
                    j = source_simplices_dict[source_simplex]
                    S[i, j] = -1 if a % 2==1 else 1   # S[i, j] = (-1)**a
        return S

    def betti_number(self, i):
        boundop_i = self.boundary_operator(i)
        boundop_ip1 = self.boundary_operator(i+1)

        if i==0:
            boundop_i_rank = 0
        else:
            try:
                boundop_i_rank = np.linalg.matrix_rank(boundop_i.toarray())
            except np.linalg.LinAlgError:
                boundop_i_rank = boundop_i.shape[1]
        try:
            boundop_ip1_rank = np.linalg.matrix_rank(boundop_ip1.toarray())
        except np.linalg.LinAlgError:
            boundop_ip1_rank = boundop_ip1.shape[1]

        return ((boundop_i.shape[1]-boundop_i_rank)-boundop_ip1_rank)

    def euler_characteristics(self):
        max_n = max(map(len, self.simplices))
        return reduce(add, map(lambda a: (-1 if a % 2==1 else 1)*self.betti_number(a), range(max_n)))
