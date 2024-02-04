import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing, make_blobs
from sklearn.cluster import KMeans

california_housing = fetch_california_housing(as_frame=True)
Number_of_Instances = 20640

Latitude = california_housing.frame["Latitude"]
Longitude = california_housing.frame["Longitude"]
MedInc = california_housing.frame["MedInc"]

# mat is the matrix to be predicted using k-means alogorithm
mat = []
for i in range(Number_of_Instances):
    mat.append([i,MedInc[i]])

km = KMeans(
    n_clusters=3, init='random',
    n_init=20, max_iter= int(Number_of_Instances/100)
)
clu = km.fit_predict(mat)
# now clustered output is in clu. let's color them for better visuals

# colors = ["blue" , "orange" , "orange"]

# _x = []
# _y = []
# _A = [[0 for i in range(Number_of_Instances)] for j in range (Number_of_Instances)]
# counter = 0
# for j in range(len(clu)):
#     _A[clu[j]].append(counter)
#     counter += 1

# for i in range(3):   
#     for j in _A[i]:    
#         _x.append(Latitude[j])
#         _y.append(Longitude[j])
#     plt.scatter(_x , _y , c=colors[i] , marker='o', edgecolor='black', s=50)


red = []
blue = []
orange = []
counter = 0

for i in clu:
    if i==0:
        red.append(counter)
    elif i==1:
        blue.append(counter)
    elif i==2:
        orange.append(counter)
    counter = counter + 1

# coloring red
redx = []
redy = []
for i in red:
    redx.append(Latitude[i])
    redy.append(Longitude[i])
plt.scatter(redx, redy, c='red',edgecolor='black', s=50)
# coloring blue
bluex = []
bluey = []
for i in blue:
    bluex.append(Latitude[i])
    bluey.append(Longitude[i])
plt.scatter(bluex, bluey, c='blue',edgecolor='black', s=50)
# coloring orange
orangex = []
orangey = []
for i in orange:
    orangex.append(Latitude[i])
    orangey.append(Longitude[i])
plt.scatter(orangex, orangey,c='orange',edgecolor='black', s=50)

plt.draw()
plt.show()