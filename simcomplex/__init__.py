__author__ = 'stephenhky'

from itertools import combinations

def facesiter(simplex):
    for i in range(len(simplex)):
        yield simplex[:i]+simplex[(i+1):]

def flattening_simplex(simplices):
    for simplex in simplices:
        for point in simplex:
            yield point

def get_allpoints(simplices):
    return set(flattening_simplex(simplices))

def faces(simplices):
    faceset = set()
    for simplex in simplices:
        numnodes = len(simplex)
        for r in range(numnodes, 0, -1):
            for face in combinations(simplex, r):
                faceset.add(tuple(sorted(face)))
    return faceset


from simcomplex.abssimcomplex import SimplicialComplex
from simcomplex.vrcomplex import VietorisRipsComplex
from simcomplex.alphacomplex import AlphaComplex