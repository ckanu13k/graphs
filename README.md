# Graphs

[![PyPI version](https://badge.fury.io/py/graphs.svg)](http://badge.fury.io/py/graphs)
[![Build Status](https://travis-ci.org/all-umass/graphs.svg?branch=master)](https://travis-ci.org/all-umass/graphs)
[![Coverage Status](https://coveralls.io/repos/all-umass/graphs/badge.svg?branch=master&service=github)](https://coveralls.io/github/all-umass/graphs?branch=master)

A library for Graph-Based Learning in Python.

Provides several types of graphs container objects,
with associated visualization, analysis, and embedding functions.

## Requirements

Requires recent versions of:

  * numpy
  * scipy
  * scikit-learn
  * matplotlib

Optional dependencies:

  * python-igraph
  * graphtool
  * networkx

Testing requires:

  * nose
  * nose-cov

## Usage example

```python
from graphs.construction import random_graph

G = random_graph([2,3,1,3,2,1,2])

print G.num_vertices()  # 7
print G.num_edges()     # 14

G.symmetrize(method='max')
X = G.isomap(num_vecs=2)

G.plot(X, directed=False, weighted=False, title='isomap embedding')()
```
