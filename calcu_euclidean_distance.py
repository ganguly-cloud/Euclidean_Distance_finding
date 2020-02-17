# -*- coding: utf-8 -*-
'''
What is euclidean distance ?

Sol : It is the most obvious way of representing distance between two points
 Its used in KNN(K-Nearest Neighbors) algo to calculate the distance b/w the
 data points.
 

Formula :
	

For points (x1,y1,z1) and (x2,y2,z2) in 3-dimensional space, the Euclidean
distance between them is (x2−x1)2+(y2−y1)2+(z2−z1)2−−−−−−−−−−−−−−−−−−−−−−−−−−−√. For example,
the Euclidean distance between (−1,2,3) and (4,0,−3) is sq.rt(25+4+36)−−−−−−−−−√=65−−√.

'''



'''Calculate euclidean _distance for KNN algo '''

from math import sqrt

plot1 = [1,3]
plot2 = [2,5]

euclidean_distance = sqrt( (plot1[0]-plot2[0])**2 +
                            (plot1[1]-plot2[1])**2 )

print euclidean_distance   # 2.2360679775
