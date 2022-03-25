"k-means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells. k-means clustering minimizes within-cluster variances (squared Euclidean distances), but not regular Euclidean distances. [...] The problem is computationally difficult (NP-hard)."

"Given a set of observations (x1, x2, ..., xn), where each observation is a d-dimensional real vector, k-means clustering aims to partition the n observations into k (≤ n) sets S = {S1, S2, ..., Sk} so as to minimize the within-cluster sum of squares (WCSS) (i.e. variance). Formally, the objective is to find:
```math
{\displaystyle {\underset {\mathbf {S} }{\operatorname {arg\,min} }}\sum _{i=1}^{k}\sum _{\mathbf {x} \in S_{i}}\left\|\mathbf {x} -{\boldsymbol {\mu }}_{i}\right\|^{2}={\underset {\mathbf {S} }{\operatorname {arg\,min} }}\sum _{i=1}^{k}|S_{i}|\operatorname {Var}
S_{i}}
```
where $μ_{i}$ is the mean of points in $S_{i}$. This is equivalent to minimizing the pairwise squared deviations of points in the same cluster:

```math
{\displaystyle {\underset {\mathbf {S} }{\operatorname {arg\,min} }}\sum _{i=1}^{k}\,{\frac {1}{|S_{i}|}}\,\sum _{\mathbf {x} ,\mathbf {y} \in S_{i}}\left\|\mathbf {x} -\mathbf {y} \right\|^{2}}
```

The equivalence can be deduced from identity 

```math
{\displaystyle |S_{i}|\sum _{\mathbf {x} \in S_{i}}\left\|\mathbf {x} -{\boldsymbol {\mu }}_{i}\right\|^{2}=\sum _{\mathbf {x} \neq \mathbf {y} \in S_{i}}\left\|\mathbf {x} -\mathbf {y} \right\|^{2}}
```

Note that, due to that the total variance is constant, this is equivalent to maximizing the sum of squared deviations between points in different clusters (between-cluster sum of squares, BCSS),[1]. This deterministic relationship is also related to the law of total variance in probability theory."

https://en.wikipedia.org/wiki/K-means_clustering

# kmeans_clustering.py

The kmeans clustering .py python script is run:

      'python3 kmeans.py k input.txt'

where k is the number of clusters and input.txt is one of the
files: 'input1.txt' (k=2), 'input2.txt' (k=2), 'input3.txt' (k=3),
or 'input4.txt' (k=4).

Remark: the output may vary the indices assignment, but the clusters are always the same, as 
is evidenced by the screenshots and gen.exe.

Example input - input3.txt: 

[input3.txt](https://github.com/Austin-Faulkner/kmeans_clustering/files/8351283/input3.txt)


Example output - output3.txt:

[output3.txt](https://github.com/Austin-Faulkner/kmeans_clustering/files/8351290/output3.txt)

Example cluster mapping in gen.exe - K_3_input3_output.jpeg:

![k_3_input3_output](https://user-images.githubusercontent.com/7588505/160138506-38ec8b62-f723-48c6-99c4-6cc00d638cfd.jpeg)
