# DBSCAN IMPLEMENTATION

* Usage: 
```
> python dbscan.py -k <min_points_neighbors> -d (0 – Supremum distance | 1 – Manhattan distance | 2 – Euclidean distance ) <file-name>.txt"
```

- Eps: Maximum radius of the neighborhood

- MinPts: Minimum number of points in an Eps-neighbourhood of that point

- Directly density reachable: A point p is deemed as directly density-reachable from another point q if p is within Epsneighborhood of q and q is identified as a core point.

- Density-connected: if there is a point O such that both, P and Q are density-reachable from O

- Core point: if it has more than a specified number of points (MinPts) within Eps.

- Border point: has fewer than MinPts within Eps, but is in the neighborhood of a core point.

- Noise(outlier) point: the points that are neither core or border points

* DBSCAN algorithm:
	1. Arbitrary select a point p
	2. Retrieve all points density-reachable from p based on Eps and MinPts
	3. If p is a core point, a cluster is formed
	4. If p is a border point, no points are density-reachable from p and DBSCAN visits the next point of the database
	5. Continue the process until all of the points have been processed


DataPoints: 
	
	x1(0,0), x2(1,0), x3(1,1), 
	x4(2,2), x5(3,1), x6(3,0), 
	x7(0,1), x8(3,2), x9(6,3)

Eps = 1, MinPts = 3. 	

First
  Calculate the N(p), Eps-neighborhood of point p
	
	D = 1
	
	If the size of N(p) is at least MinPts, then p is said to be a core point.
	
	
	N(x1) = {x1, x2, x7} core point 
	N(x2) = {x2, x1, x3} core point 
	N(x3) = {x3, x2, x7} core point 
	N(x4) = {x4, x8} 	 border point
	N(x5) = {x5, x6, x8} core point 
	N(x6) = {x6, x5} 	 border point
	N(x7) = {x7, x1, x3} core point 
	N(x8) = {x8, x4, x5} core point 
	N(x9) = {x9} noise(outlier)
	
DBSCAN algorithm example:

		choose x1
		x1: {x2, x3, x7}
		x1 is a core point
		cluster_1 = { x1, x2, x3 ,x7 }
		
		choose x5
		x5: {x4, x6, x8}
		x5 is a core point
		cluster_2: {x5, x4, x8, x6}
		
		choose x9
		x9 is a noise point
		noise points do NOT belong to any clusters.
		
		Thus the algorithm stops here.
