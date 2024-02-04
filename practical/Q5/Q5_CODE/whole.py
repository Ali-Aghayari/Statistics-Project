import scipy
import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx

# all codes below have been executed at least one time
# if you ever read comments or variable names and didn't understand the meaning of it
# please check information available in jupyter notebook file attached alongside this file
# to check specific functions , uncomment them to avoid time consuming problems
# enjoy clustering at it's best

# ========================= q17 =========================
def init_graph(n , p):
    g = [[0 for col in range(n)] for row in range(n)]
    for row in range(n):
        for col in range(n):
            if (col>row):
                g[row][col] = scipy.stats.bernoulli.rvs(p, loc=0 ,size=1 , random_state=None)[0]
            elif (col<row):
                g[row][col] = g[col][row]   # symmetric attribute of matrix
    return g

def cnt_adjacencies (g):
    return (np.array(g)).sum() / 2

def sapply_N (N , n , p):
    mean = 0
    for i in range (N):
        graph = init_graph(n, p)
        cnt = cnt_adjacencies(graph)
        print(cnt)
        mean += cnt
    print(mean/N)

#sapply_N (10 , 1000 , 0.0034)   

# ========================= q18 =========================
def cnt_adjacents_of_vertex (g , v_index):
    return (np.array(g[v_index])).sum()

# a function to simply cnt_same_colors of a given graph g with chance p and number of n
def cnt_same_colors (g , p , n):
    L = (n-1)*p
    out = 0
    for i in range(n):
        if (cnt_adjacents_of_vertex(g, i) >= L):
            out += 1
    return out


def sapply_N_q18(N , n , p):
    mean = 0
    for i in range (N):
        graph = init_graph(n, p)
        cnt = cnt_same_colors(graph , p , n)
        #print(cnt)
        mean += cnt
    print(mean/N)

#sapply_N_q18(10 , 1000 , 0.00016)


# ========================= q19 =========================

def cnt_transitive_and_chained(g , n):
    transitive = chained = 0
    for row in range(n):
        for col in range(row+1 , n):
            val_to_add = 0
            for s in range (n):
                if (g[row][s]==1 & g[row][s] == g[col][s] & (s!=row & s!=col)):
                    val_to_add = 1 
            if g[row][col] == 1:
                transitive += val_to_add
            else:
                chained += val_to_add
    return transitive,chained

def sapply_N_q19(N , n , p):
    mean_chained = mean_transitive = 0
    for i in range (N):
        graph = init_graph(n, p)
        cnt1 , cnt2 = cnt_transitive_and_chained(graph, n)
        mean_transitive += cnt1
        mean_chained += cnt2
    print("mean_transitive : " , mean_transitive/N)
    print("mean_chained : " , mean_chained/N)

#sapply_N_q19(5, 100 , 0.01)


#========================= q20 =========================

def cnt_adjacents_of_adjacents_vertex (g , n , v_index):
    out = 0
    row = np.array(g)[v_index,:]
    for i in range(n):
        if (row[i]==1): 
            out += cnt_adjacents_of_vertex(g, i)
            # out -= 1    # adjacency with v_index is better not to be counted
    return out   

def sapply_N_q20 (N , n , p):
    avg = 0
    for i in range(N):
        g = init_graph(n,p) 
        for j in range(n):
            avg += cnt_adjacents_of_adjacents_vertex(g, n , j)
    avg = avg / 2   # counted twice
    print(avg / (2*n)) 

    return avg      

#sapply_N_q20(1, 1000 , 0.5)


#========================= q21 =========================

def cnt_avg_dist_in_graph (g , n):
    avg = 0
    for i in range(n):
        for j in range(n):
            if (i==j):
                continue
            avg += nx.shortest_path_length(g,i,j)
    return (avg / (n*(n-1)))

def sapply_N_q21(N , n , p):
    for i in range(N):
        g = nx.binomial_graph(n , p)
        while (nx.is_connected(g) != 1):
            g = nx.binomial_graph(n , p)
        # reached a connected graph of g
        print(cnt_avg_dist_in_graph(g, n))
        nx.draw(g , with_labels=True)
        plt.draw()
        plt.show()

# sapply_N_q21(1 , 1000 , 0.033)
             

#========================= q22 =========================

def longest_path_length(g , n):
    longest_path = 0
    for i in range(n):
        for j in range(n):
            if (i==j):
                continue
            longest_path = max(nx.shortest_path_length(g,i,j) , longest_path)
    return longest_path

def sapply_N_q22(N , n , p):
    avg = 0
    for i in range(N):
        g = nx.binomial_graph(n,p)
        while (nx.is_connected(g) != 1):
            g = nx.binomial_graph(n,p)
        avg += longest_path_length(g,n)
    print(avg / N)
    return (avg / N)

#sapply_N_q22(100, 50 , 0.34)        

#========================= q23 =========================

def q23_to_avoid_run():
    pair = []
    longest_path = []
    for n in range (10 , 201 , 10):
        pair.append(n)
        longest_path.append(sapply_N_q22(10, n, 0.34))

    plt.stem(pair , longest_path)
    plt.draw()
    plt.show()

#========================= q24 =========================

def cnt_relation_triangles_graph (g , n):
    out = 0
    for i in range(n):
        for j in range(i+1 , n):
            if (g.has_edge(i,j)==0):
                continue
            for k in range (j+1 , n):
                if (g.has_edge(i,j)==g.has_edge(j,k) & g.has_edge(j,k)==g.has_edge(i,k)):
                    out += 1
    return out

def sapply_N_q24(N, n, p):
    avg = 0
    for i in range(N):
        g = nx.binomial_graph(n , p)
        while (nx.is_connected(g) != 1):
            g = nx.binomial_graph(n , p)
        avg += cnt_relation_triangles_graph(g, n)
    print(avg/N)
    return avg/N

#sapply_N_q24(100 , 100 , 0.34)

#========================= q25 =========================

def sapply_q25():
    x = []
    y = []
    for n in range (10 , 101 , 10):
        x.append(n)
        y.append(sapply_N_q24(1, n, 60/(n**2)))
    plt.stem(x,y)
    plt.draw()
    plt.show()
# sapply_q25()


#========================= q26 =========================

def sapply_q26(p):
    x = []
    y = []
    for n in range (10 , 101 , 10):
        x.append(n)
        y.append(sapply_N_q24(1, n, p))
    plt.stem(x,y)
    plt.draw()
    plt.show()

#sapply_q26(0.34)
 
#========================= q27 =========================

def sapply_q27():
    x = []
    y = []
    for n in range (50 , 1201 , 50):
        x.append(n)
        y.append(sapply_N_q24(1, n, 49/n))
    plt.stem(x,y)
    plt.draw()
    plt.show()

#sapply_q27()

#========================= q27_cdf =========================

def sapply_q27_cdf():
    x = []
    y = []
    cnt = 0
    for n in range (50 , 1201 , 50):
        x.append(n)
        cnt += sapply_N_q24(1, n, 49/n)
        y.append(cnt)
    plt.stem(x,y)
    plt.draw()
    plt.show()

#sapply_q27_cdf()