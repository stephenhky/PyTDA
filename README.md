# PyTDA - Topological Data Analysis (TDA) for Python

## Important Notice
This repository is NOT a Python package. Codes in this
repository are for demonstration and described in the blog
entries listed below. And the codes in this repository run
in Python 2.7 only.

However, there will be an optimized
code found in the package [`mogutda`](https://pypi.org/project/mogutda/), and
you can refer to the codes in my another repository: [MoguTDA](https://github.com/stephenhky/MoguTDA)
You can also install the package `mogutda` by typing
on the command prompt:

```
pip install -U mogutda
```

The package `mogutda` runs in Python 2.7, 3.5, and 3.6.


## Introduction
PyTDA contains Python codes that demonstrate the numerical calculation
of algebraic topology in an application to topological data analysis 
(TDA).

Topological data analysis aims at studying the shapes of the data, and
draw some insights from them. A lot of machine learning algorithms deal 
with distances, which are extremely useful, but they miss the 
information the data may carry from their geometry.

## Demo Codes and Blog Entries
Codes in this repository are demo codes for a few entries of my blog,
[Everything about Data Analytics](https://datawarrior.wordpress.com/),
and the corresponding entries are:

* [Starting the Journey of Topological Data Analysis (TDA)](https://datawarrior.wordpress.com/2015/08/03/tda-1-starting-the-journey-of-topological-data-analysis-tda/) (August 3, 2015)
* [Constructing Connectivities](https://datawarrior.wordpress.com/2015/09/14/tda-2-constructing-connectivities/) (September 14, 2015)
* [Homology and Betti Numbers](https://datawarrior.wordpress.com/2015/11/03/tda-3-homology-and-betti-numbers/) (November 3, 2015)
* [Topology in Physics and Computing](https://datawarrior.wordpress.com/2015/11/10/mathanalytics-6-topology-in-physics-and-computing/) (November 10, 2015)
* [Persistence](https://datawarrior.wordpress.com/2015/12/20/tda-4-persistence/) (December 20, 2015)
* [Topological Phases](https://datawarrior.wordpress.com/2016/10/06/topological-phases/) (October 6, 2016)
* [moguTDA: Python package for Simplicial Complex](https://datawarrior.wordpress.com/2018/07/02/mogutda-python-package-for-simplicial-complex/) (July 2, 2018)

## Wolfram Demonstration
Richard Hennigan put a nice Wolfram Demonstration online explaining what
the simplicial complexes are, and how homologies are defined:

* [Simplicial Homology of the Alpha Complex](http://demonstrations.wolfram.com/SimplicialHomologyOfTheAlphaComplex/)

## Other TDA Packages
It is recommended that for real application, you should use the following packages
for efficiency, because my codes serve the pedagogical purpose only.

### C++
* [Dionysus](http://www.mrzv.org/software/dionysus/)
* [PHAT](https://bitbucket.org/phat-code/phat)

### Python
* [mogutda](https://pypi.org/project/mogutda/)
* [Dionysus](http://www.mrzv.org/software/dionysus/python/overview.html)

### R
* [TDA](https://cran.r-project.org/web/packages/TDA/index.html) (article: [\[arXiv\]](http://arxiv.org/abs/1411.1830))

## References
* Afra J. Zomorodian. *Topology for Computing* (New York, NY: Cambridge University Press, 2009). [\[Amazon\]](https://www.amazon.com/Computing-Cambridge-Monographs-Computational-Mathematics/dp/0521136091)
* Afra J. Zomorodian. "Topological Data Analysis," *Proceedings of Symposia in Applied Mathematics* (2011). [\[link\]](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.261.1298)
* Afra Zomorodian, Gunnar Carlsson, “Computing Persistent Homology,” *Discrete Comput. Geom.* 33, 249-274 (2005). [\[pdf\]](http://geometry.stanford.edu/papers/zc-cph-05/zc-cph-05.pdf) 
* Gunnar Carlsson, “Topology and Data”, *Bull. Amer. Math. Soc.* 46, 255-308 (2009). [\[link\]](http://www.ams.org/journals/bull/2009-46-02/S0273-0979-09-01249-X/)
* P. Y. Lum, G. Singh, A. Lehman, T. Ishkanov, M. Vejdemo-Johansson, M. Alagappan, J. Carlsson, G. Carlsson, “Extracting insights from the shape of complex data using topology”, *Sci. Rep.* 3, 1236 (2013). [\[link\]](http://www.nature.com/srep/2013/130207/srep01236/full/srep01236.html)
* Robert Ghrist, “Barcodes: The persistent topology of data,” *Bull. Amer. Math. Soc.* 45, 1-15 (2008). [\[pdf\]](http://www.ams.org/journals/bull/2008-45-01/S0273-0979-07-01191-3/S0273-0979-07-01191-3.pdf)
