#N — количество вершин;
#S — номер стартовой вершины (отсчитывая от нуля);
#matrix — матрица смежности исходного графа, где несуществующие рёбра имеют бесконечный вес;
#В данном случае бесконечность равна 1000000;

def Dijkstra(N, S, matrix):
	valid = [True]*N
	weight = [1000000]*N
	weight[S] = 0
	for i in range(N):
		min_weight = 1000001
		ID_min_weight = -1
		for j in range(N):
			if valid[j] and weight[j] < min_weight:
				min_weight = weight[j]
				ID_min_weight = j
		for z in range(N):
			if weight[ID_min_weight] + matrix[ID_min_weight][z] < weight[z]:
				weight[z] = weight[ID_min_weight] + matrix[ID_min_weight][z]
		valid[ID_min_weight] = False
	return weight
