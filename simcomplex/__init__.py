__author__ = 'stephenhky'

def facesiter(simplex):
    for i in range(len(simplex)):
        yield simplex[:i]+simplex[(i+1):]

def flattening_simplex(simplices):
    for simplex in simplices:
        for point in simplex:
            yield point

def get_allpoints(simplices):
    return set(flattening_simplex(simplices))

from simcomplex.abssimcomplex import SimplicialComplex
from simcomplex.vrcomplex import VietorisRipsComplex
from simcomplex.alphacomplex import AlphaComplex