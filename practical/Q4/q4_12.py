import random
import numpy as np
from numpy.linalg import eig
import math
import cmath

n = 1000
p = 0.1
q = 0.01

def algorithm1 (n , p , q):
    # random uniform distribution of all people
    all_people = [n]
    for i in range(n):
        all_people.append(random.randint(1, 2))

    # allocating A
    A = []
    for i  in range(n):
        row = []
        for j in range(n):
            to_append = 0
            if all_people[i]==all_people[j]:    # for p = 0.1
                if random.randint(1,10) == 1:
                    to_append = 1
            else:
                if random.randint(1,100) == 1:  # for q = 0.01
                    to_append = 1
            row.append(to_append)
        A.append(row)

    # allocating W    
    W = []
    for i in range(n):
        row = []
        for j in range(0,n):
            if all_people[i]==all_people[j]:
                row.append(p)
            else:
                row.append(q)
        W.append(row)

    # calculating lw
    lw = []
    index = 0
    for i in W:
        sum = 0
        row = []
        for j in i:
            sum += j
            row.append(-j)
        row[index] += sum
        lw.append(row)
        index = index + 1
    # now we start working with numpy arrays
    W_np = np.array(lw)
    w1 , v1 = eig(W_np)   # w1 has eigenvectors of lw
                        # v1 has eigenvalues (normalized) of lw (same order as w1)


    #calculating la
    la = []
    index = 0
    for i in A:
        sum = 0
        row = []
        for j in i:
            sum += j
            row.append(-j)
        row[index] += sum
        la.append(row)
        index = index + 1

    A_np = np.array(la)
    w2 , v2=eig(A_np)   # w2 has eigenvectors of la
                        # v2 has eigenvalues (normalized) of lw (same order as w2)


    # now as suggested in question itself, we need eigenvectors of la and lw with lowest eigenvalues
    # after finding them, we gonna report the error of clustering using la and lw 
    # (for significantly large n values, the error should be unnoticable)


    minValueW1 = w1[0]
    minVectorW1 = []
    minValueW2 = w1[0]
    minVectorW2 = []
    # finding least eigenvalue and it's responding eigenvector
    counter = 0
    index = 0
    for i in w1:
        if i<minValueW1:
            minValueW1 = i
            index = counter
        counter = counter + 1
    minVectorW1 = v1[index]
    # finding second least eigenvalue and it's responding eigenvector
    counter = 0
    index = 0
    for i in w1:
        if (i<minValueW2 and i>minValueW1):
            minValueW2 = i
            index = counter
        counter = counter + 1
    minVectorW2 = v1[index]

    # now for la
    minValueA1 = w2[0]
    minVectorA1 = []
    minValueA2 = w2[0]
    minVectorA2 = []
    counter = 0
    index = 0
    # finding least eigenvalue and it's responding eigenvector
    for i in w2:
        if i<minValueA1:
            minValueA1 = i
            index = counter
        counter = counter + 1
    minVectorA1 = v2[index]
    # finding second least eigenvalue and it's responding eigenvector
    counter = 0
    index = 0
    for i in w2:
        if (i<minValueA2 and i>minValueA1):
            minValueA2 = i
            index = counter
        counter = counter + 1
    minVectorA2 = v2[index]

    # print("eigenvectors are :")
    # print(minVectorA1)
    # print(minVectorA2)
    # print(minVectorW1)
    # print(minVectorW2)

    # calculating error based on first pair of eigenvectors
    sum = 0
    index = 0
    for i in minVectorW1:
        x = (i-minVectorA1[index])**2
        sum += x
        index += 1
    print("first error :  ",math.sqrt(sum.real))

    # calculating error based on second pair of eigenvectors
    sum = 0
    index = 0
    for i in minVectorW2:
        x = (i-minVectorA2[index])**2
        sum += x
        index += 1
    print("second error : ",math.sqrt(sum.real))


for i in range (200 , 1001 , 100):
    algorithm1(i, p, q)