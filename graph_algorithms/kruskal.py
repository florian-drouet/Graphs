class kruskal_algorithm:

    def __init__(self):
        self.parent = dict()
        self.minimum_spanning_tree = []
        self.cost = 0

    def make_set(self, vertex):
        '''
        La fonction make_set permet de créer un singleton 
        '''
        self.parent[vertex] = None

    def find(self, vertex):
        '''
        La fonction find permet de remonter l'arbre à partir d'un vertex jusqu'à la racine de l'arbre (une racine nulle n'a
        pas de parent). Elle renvoie le parent du vertex en question.
        '''
        if self.parent[vertex] == None:
            return vertex
        return self.find(self.parent[vertex])

    def union(self, vertex1, vertex2):
        '''
        La fonction union permet de réunir deux vertices par leurs racines
        '''
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            self.parent[root2] = root1

    def kruskal(self, edges, vertices, clusters=1):
        '''
        Ci-après la deuxième version de l'algorithme de Kruskal codée via la technique union-find.
        
        On commence par créer un singleton par vertex puis on trie les edges (un edge est un triplé composé de la façon
        suivante : vertex1, vertex2, poids de l'edge vertex1 vers vertex2)
        
        Dans cette liste d'edge trié on cherche les racines des vertices 1 et 2 (pour chaque edge de la liste des edges triés)
        via la fonction find. Puis, s'ils n'ont pas la même racine, alors on rassemble les deux vertices via la fonction 
        union puis on rajoute l'edge dans l'edge de recouvrement de poids minimal.
        '''
        for vertex in vertices:
            self.make_set(vertex)
        edges_sorted = sorted(edges,key=lambda cost: cost[2])
        for edge in edges_sorted:
            if self.find(edge[0]) != self.find(edge[1]):
                self.union(edge[0], edge[1])
                self.minimum_spanning_tree.append(edge)
                self.cost = self.cost + edge[2]
            if list(self.parent.values()).count(None) == clusters:
                break
        return self.minimum_spanning_tree, self.cost

if __name__ == "__main__":
    edges = [[1,5,10],[3,5,20],[2,8,30],[1,3,35],[6,7,40],[6,8,50],[7,8,75],
            [2,6,80],[2,4,100],[2,5,150],[4,7,180],[2,3,200],[3,4,200],[1,4,300],[2,7,300]]
    vertices = [1,2,3,4,5,6,7,8]
    clusters = 2
    kruskal_result = kruskal_algorithm().kruskal(edges, vertices, clusters=1)
    print(kruskal_result[0])
