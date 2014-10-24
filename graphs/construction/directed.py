import numpy as np
from sklearn.metrics.pairwise import paired_distances
from graphs import Graph, plot_graph
from neighbors import neighbor_graph


def jeff_graph(trajectories, k=5, verbose=False, pruning_thresh=0, return_coords=False):
  '''Directed graph construction alg. from Johns & Mahadevan, ICML '07.
  trajectories: list of NxD arrays of ordered states
  '''
  X = np.vstack(trajectories)
  G = neighbor_graph(X, k=k, symmetrize=False)
  if pruning_thresh > 0:
    traj_len = map(len, trajectories)
    G = jeff_prune_edges(G, X, traj_len, pruning_thresh, verbose=verbose)
  if return_coords:
    return G, X
  return G


def jeff_prune_edges(G, X, traj_lengths, pruning_thresh=0.1, verbose=False):
  '''Prune edges in graph G via cosine distance with trajectory edges.'''
  W = G.matrix(dense=True).copy()
  degree = G.degree(kind='out', unweighted=True)
  i = 0
  num_bad = 0
  for n in traj_lengths:
    s,t = np.nonzero(W[i:i+n-1])
    graph_edges = X[t] - X[s+i]
    traj_edges = np.diff(X[i:i+n], axis=0)
    traj_edges = np.repeat(traj_edges, degree[i:i+n-1], axis=0)
    theta = paired_distances(graph_edges, traj_edges, 'cosine')
    bad_edges = theta > pruning_thresh
    W[s[bad_edges],t[bad_edges]] = 0
    if verbose:
      num_bad += np.count_nonzero(bad_edges)
    i += n
  if verbose:
    print 'removed %d bad edges' % num_bad
  return Graph.from_adj_matrix(W)
