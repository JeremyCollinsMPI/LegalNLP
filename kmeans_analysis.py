from sklearn.cluster import KMeans

def kmeans_analysis(data):
  kmeans = KMeans(n_clusters=20, random_state=1)
  kmeans.fit(data)
  return kmeans

