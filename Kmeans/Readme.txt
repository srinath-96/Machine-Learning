### CONCEPT

Kmeans Algorithm is an unsupervised clustering algorithm. K-means uses an iterative refinement method to produce its final clustering based on the number of clusters defined by the user (represented by the variable *K*) and the dataset. 

K-means starts off with arbitrarily chosen data points as proposed **means** of the data groups, and iteratively recalculates new means in order to converge to a final clustering of the data points.

When you define the value of K you are actually telling the algorithm how many means or *centroids* you want . A **centroid** is a data point that represents the center of the cluster , and it might not necessarily be a member of the dataset. 



### EUCLIDEAN DISTANCE

Euclidean distance of a point in n-dimensional space is given by the Pythagorean formula as below :

![image-20201002194239272](C:\Users\srina\AppData\Roaming\Typora\typora-user-images\image-20201002194239272.png)

### OPTIMIZATION PROBLEM REGARDING KMEANS

The Kmeans algorithm is minimizing a Loss function to get an optimized output, that is the centers of the cluster.

<img src="C:\Users\srina\AppData\Roaming\Typora\typora-user-images\image-20201002194529306.png" alt="image-20201002194529306" style="zoom:80%;" />

### STEPS TO PERFORM THE ALGORITHM

1. K centroids are created randomly (based on the predefined value of K)

2. K-means allocates every data point in the dataset to the nearest centroid (minimizing Euclidean distances between them), meaning that a data point is considered to be in a particular cluster if it is closer to that cluster’s centroid than any other centroid

3. Then K-means recalculates the centroids by taking the mean of all data points assigned to that centroid’s cluster, hence reducing the total intra-cluster variance in relation to the previous step. The “means” in the K-means refers to averaging the data and finding the new centroid

4. The algorithm iterates between steps 2 and 3 until some criteria is met
Source:### CONCEPT

Kmeans Algorithm is an unsupervised clustering algorithm. K-means uses an iterative refinement method to produce its final clustering based on the number of clusters defined by the user (represented by the variable *K*) and the dataset. 

K-means starts off with arbitrarily chosen data points as proposed **means** of the data groups, and iteratively recalculates new means in order to converge to a final clustering of the data points.

When you define the value of K you are actually telling the algorithm how many means or *centroids* you want . A **centroid** is a data point that represents the center of the cluster , and it might not necessarily be a member of the dataset. 



### EUCLIDEAN DISTANCE

Euclidean distance of a point in n-dimensional space is given by the Pythagorean formula as below :

![image-20201002194239272](C:\Users\srina\AppData\Roaming\Typora\typora-user-images\image-20201002194239272.png)

### OPTIMIZATION PROBLEM REGARDING KMEANS

The Kmeans algorithm is minimizing a Loss function to get an optimized output, that is the centers of the cluster.

<img src="C:\Users\srina\AppData\Roaming\Typora\typora-user-images\image-20201002194529306.png" alt="image-20201002194529306" style="zoom:80%;" />

### STEPS TO PERFORM THE ALGORITHM

1. K centroids are created randomly (based on the predefined value of K)

2. K-means allocates every data point in the dataset to the nearest centroid (minimizing Euclidean distances between them), meaning that a data point is considered to be in a particular cluster if it is closer to that cluster’s centroid than any other centroid

3. Then K-means recalculates the centroids by taking the mean of all data points assigned to that centroid’s cluster, hence reducing the total intra-cluster variance in relation to the previous step. The “means” in the K-means refers to averaging the data and finding the new centroid

4. The algorithm iterates between steps 2 and 3 until some criteria is met

   

SOURCE:[Kmeans]:https://www.kdnuggets.com/2019/05/guide-k-means-clustering-algorithm.html
   



