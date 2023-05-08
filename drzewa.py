import numpy as np
from collections import Counter


class Node:
  def __init__(self, feature=None, threshold=None, left=None, right=None,*, value=None):
    self.feature = feature
    self.threshold = threshold
    self.left = left
    self.right = right
    self.value = value

  def is_leaf_node(self):
    return self.value is not None

class DecisionTree:
  def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
    self.min_samples_split=min_samples_split
    self.max_depth=max_depth
    self.n_features=n_features
    self.root=None
    
  def fit(self, X, y):
        if self.n_features:
            self.n_features = min(self.n_features, X.shape[1])
        else:
            self.n_features = X.shape[1]

        self.root = self._grow_tree(X, y)
              

  def _grow_tree(self, X, y, depth=0):
    sampleNum , featureNum = X.shape 
    labels = len(set(y))
    bestGain = -1
    featureIndex = np.random.choice(featureNum, self.n_features, replace=False)
    split = splitThreshold = None

    if depth >= self.max_depth:
        counter = Counter(y)
        strongestValue = counter.most_common(1)[0][0]
        return Node(value=strongestValue)

    if sampleNum < self.min_samples_split:
        counter = Counter(y)
        strongestValue = counter.most_common(1)[0][0]
        return Node(value=strongestValue)

    if labels == 1:
        counter = Counter(y)
        strongestValue = counter.most_common(1)[0][0]
        return Node(value=strongestValue)

    for i in featureIndex:
        values = X[:, i]
        thresholdSet = sorted(set(values))
        for j in range(1, len(thresholdSet)):
            middlePoint = (thresholdSet[j] + thresholdSet[j - 1]) / 2
            informationGain = self._information_gain(y, values, middlePoint)
            if informationGain > bestGain:
                bestGain = informationGain
                split = i
                splitThreshold = middlePoint

    if split is None or splitThreshold is None:
        counter = Counter(y)
        strongestValue = counter.strongest(1)[0][0]
        return Node(value=strongestValue)

    leftIndices, rightIndices = self._split(X[:, split], splitThreshold)

    return Node(split, splitThreshold,
                left=self._grow_tree(X[leftIndices, :], y[leftIndices], depth + 1),
                right=self._grow_tree(X[rightIndices, :], y[rightIndices], depth + 1))
                
       
  def _best_split(self, X, y, feat_idxs):
    bestGain = -1
    split, splitThreshold = None, None

    for i in feat_idxs:
        values = X[:, i]
        sortedValues = np.sort(values)
        for j in range(1, len(sortedValues)):
            middlePoint = (sortedValues[j] + sortedValues[j - 1]) / 2
            informationGain = self._information_gain(y, values, middlePoint)
            if informationGain > bestGain:
                bestGain = informationGain
                split = i
                splitThreshold = middlePoint

    return split, splitThreshold


  def _information_gain(self, y, X_column, threshold):
    parentEntropy = self._entropy(y)

    leftMask = X_column <= threshold
    rightMask = X_column > threshold

    leftLabels = y[leftMask]
    rightLabels = y[rightMask]

    leftCount = len(leftLabels)
    rightCount = len(rightLabels)

    if leftCount == 0 or rightCount == 0:
        return 0

    leftEntropy = self._entropy(leftLabels)
    rightEntropy = self._entropy(rightLabels)

    childEntropy = (leftCount / len(y)) * leftEntropy + (rightCount / len(y)) * rightEntropy

    return parentEntropy - childEntropy
    

  def _split(self, X_column, split_thresh):
    sortedIndices = np.argsort(X_column)
    sortedValues = X_column[sortedIndices]

    split_index = np.searchsorted(sortedValues, split_thresh, side='right')

    leftIndices = sortedIndices[:split_index]
    rightIndices = sortedIndices[split_index:]

    return leftIndices, rightIndices
    

  def _entropy(self, y):
    hist = np.bincount(y)
    ps = hist / len(y)
    return -np.sum([p * np.log(p) for p in ps if p>0])
    

  def _traverse_tree(self, x, node):
    if node.is_leaf_node():
      return node.value
    
    if x[node.feature] <= node.threshold:
      return self._traverse_tree(x,node.left)
    else:
      return self._traverse_tree(x,node.right)
      

  def predict(self, X):
    return np.array([self._traverse_tree(x, self.root) for x in X])
