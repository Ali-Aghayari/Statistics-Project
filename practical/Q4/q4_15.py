import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from numpy.linalg import eig
from sklearn.cluster import KMeans
from scipy.sparse.csgraph import laplacian

G = nx.karate_club_graph()
volume = int(G.number_of_edges() / 2)
edges = []
for edge in G.edges:
    edges.append([edge[0] , edge[1]])

# adjacency matrix but not as a numpy array
adj = []
for i in range(0,34):
    row = []
    for j in range(0,34):
        if edges.count([i,j])!=0 or edges.count([j,i])!=0:
            row.append(1)
        else:
            row.append(0)
    adj.append(row)

A = np.array([adj[0],adj[1],adj[2],adj[3],adj[4],adj[5],adj[6],adj[7],adj[8],adj[9],adj[10],adj[11],adj[12],adj[13],adj[14],adj[15],adj[16],adj[17],adj[18],adj[19],adj[20],adj[21],adj[22],adj[23],adj[24],adj[25],adj[26],adj[27],adj[28],adj[29],adj[30],adj[31],adj[32],adj[33]])
L = np.diag(A.sum(axis=1)) - A
# getting eigenvalues and eigenvectors
vals , vecs = eig(L)
vecs = vecs[:,np.argsort(vals)]
vals = vals[np.argsort(vals)]

def color_for_k (k):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(vecs[:,1:k])
    colors = kmeans.labels_
    x_1 = []
    y_1 = []
    x_2 = []
    y_2 = []
    x_3 = []
    y_3 = []
    x_4 = []
    y_4 = []
    counter = 0
    for i in colors:
        if i==0:
            x_1.append(counter)
            y_1.append(G.degree(counter))
        elif i==1:
            x_2.append(counter)
            y_2.append(G.degree(counter))
        elif i==2 and k>=2:
            x_3.append(counter)
            y_3.append(G.degree(counter))
        elif i==3 and k>=3:
            x_4.append(counter)
            y_4.append(G.degree(counter))
        counter = counter + 1

    plt.scatter(x_1, y_1, c='blue',edgecolor='black')
    plt.scatter(x_2, y_2,c='orange',edgecolor='black')
    if (k>=3):
        plt.scatter(x_3, y_3,c='green',edgecolor='black')
    if (k==4):
        plt.scatter(x_4, y_4,c='red',edgecolor='black')
    plt.show()

color_for_k(4)