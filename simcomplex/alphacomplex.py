__author__ = 'stephenhky'

from scipy.spatial import Delaunay, distance
from simcomplex import SimplicialComplex
from simcomplex import facesiter, get_allpoints
from operator import or_
from functools import partial

def contain_detachededges(simplex, distdict, epsilon):
    if len(simplex)==2:
        return (distdict[simplex[0], simplex[1]] > 2*epsilon)
    else:
        return reduce(or_, map(partial(contain_detachededges, distdict=distdict, epsilon=epsilon), facesiter(simplex)))

class AlphaComplex(SimplicialComplex):
    def __init__(self, points, epsilon, labels=None, distfcn=distance.euclidean):
        self.pts = points
        self.labels = range(len(self.pts)) if labels==None or len(labels)!=len(self.pts) else labels
        self.epsilon = epsilon
        self.distfcn = distfcn
        self.import_simplices(self.construct_simplices(self.pts, self.labels, self.epsilon, self.distfcn))

    def calculate_distmatrix(self, points, labels, distfcn):
        distdict = {}
        for i in range(len(labels)):
            for j in range(len(labels)):
                distdict[(labels[i], labels[j])] = distfcn(points[i], points[j])
        return distdict

    def construct_simplices(self, points, labels, epsilon, distfcn):
        delaunay = Delaunay(points)
        delaunay_simplices = map(tuple, delaunay.simplices)
        distdict = self.calculate_distmatrix(points, labels, distfcn)

        simplices = []
        for simplex in delaunay_simplices:
            faces = list(facesiter(simplex))
            detached = map(partial(contain_detachededges, distdict=distdict, epsilon=epsilon), faces)
            if reduce(or_, detached):
                if len(simplex)>2:
                    for face, notkeep in zip(faces, detached):
                        if not notkeep:
                            simplices.append(face)
            else:
                simplices.append(simplex)
        simplices = map(lambda simplex: tuple(sorted(simplex)), simplices)
        simplices = list(set(simplices))

        allpts = get_allpoints(simplices)
        for point in (set(labels)-allpts):
            simplices += [(point,)]

        return simplices